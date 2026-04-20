from edu_assistant.api import app
from fastapi.testclient import TestClient

client = TestClient(app)

response = client.post(
    "/ask",
    data={
        "role":"math_tutor",
        "template":"tutor_quick_answer",
        "question": "Что такое число Пи",
    },
)

print(response.text) 


