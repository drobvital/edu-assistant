from edu_assistant.api import app
from fastapi.testclient import TestClient

client = TestClient(app)

response = client.post(
    "/ask",
    data={
        "role":"math_tutor",
        "template":"tutor_quick_answer",
        "question": "Упрости выражение: x^2-x(x+1)+2(0.5x-1)+2",
    },
)

print(response.text) 


