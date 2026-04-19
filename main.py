from edu_assistant.assistant import create_response


# Prepare prompt for LLM
INPUT_PROMPT = "Чему равен квадрат гипотенузы в теореме пифагора"

# Call assistant
response = create_response(
    llm_key = "ollama",
    role = "math_tutor",
    template = "tutor_quick_answer",
    prompt = INPUT_PROMPT,
)

print(response) 


