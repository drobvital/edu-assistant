from dotenv import load_dotenv
from edu_assistant.config import Config
from edu_assistant.llm_client import get_llm_client

# Load environment variables from .env file
load_dotenv()

# Prepare prompt for LLM
INPUT_PROMPT = "Кто ты?"

# Read config from YAML file
config = Config.from_yaml_file("config.yml")
llm_config = config.llms["ollama"]

# Create llm_client
llm_client = get_llm_client(llm_config)

# Вызов llm_client Responses API передав промпт как input
response = llm_client.responses.create(
    model = llm_config.model,
    input = INPUT_PROMPT
)
 

print(response.output_text)
