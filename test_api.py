import json
from fastapi.testclient import TestClient
from FastAPI import app 

client = TestClient(app)

def test_translate():
    # Тестирование успешного запроса
    data = {"text": "Hello"}
    response = client.post("/translate", json=data)
    assert response.status_code == 200
    assert "translation" in response.json()

def test_translate_error():
    # Тестирование ошибки сервера
    data = {"text": ""}
    response = client.post("/translate", json=data)
    assert response.status_code == 500

    # Тестирование ошибки запроса
    data = {"wrong_key": "Hello"}
    response = client.post("/translate", json=data)
    assert response.status_code == 422
