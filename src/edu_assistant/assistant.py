from dotenv import load_dotenv
from loguru import logger

from edu_assistant.config import Config, RoleType, TemplateType
from edu_assistant.llm_client import get_llm_client

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
