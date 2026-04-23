from dotenv import load_dotenv
from loguru import logger

from edu_assistant.config import Config, RoleType, TemplateType
from edu_assistant.llm_client import get_llm_client
from edu_assistant.tools.formula import extract_and_solve_trailing_formula

# Load environment variables from .env file
load_dotenv()

def create_response(
        llm_key: str,
        role: RoleType,
        template: TemplateType,
        prompt: str,
        ) -> str:
    #прочитать конфиг из YAML файла
    config = Config.from_yaml_file("config.yml")

    #Взять llm конфиг по ключу из config.llms
    llm_config = config.llms[llm_key]

    #создать llm_client, предоставив llm_config
    llm_client = get_llm_client(llm_config=llm_config)

    #используя config, отрендерить инструкцию для роли и шаблон системного промпта
    instructions = config.render_system_instructions(role=role, template=template)
    #обработка в случае наличия математического выражения в промте
    if role == "math_tutor":
        solution = extract_and_solve_trailing_formula(prompt)
        logger.debug(f"Extracted solution: {solution}")
        logger.debug(f"Instructions before: {instructions}")
        if solution:
            instructions += f"\n\nВажно!Не пытайся считать формулу,используй уже посчитанный результат:{solution}"
        logger.debug(f"Instructions after: {instructions}")    

    #вывести на экран инструкцию,используя logger.debug
    logger.debug(f"LLM instructions: {instructions}")

    #вызвать llm_client Responses API с аргументами input, instructions
    response = llm_client.responses.create(
        model = llm_config.model,
        instructions = instructions,
        input = prompt,
        max_output_tokens = llm_config.max_output_tokens
    )

    #вернуть output_text из ответа
    return response.output_text
