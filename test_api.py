import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_translate_success():
    response = client.post("/translate", json={"text": "Hello, world!"})
    assert response.status_code == 200
    assert "translation" in response.json()

def test_translate_error():
    response = client.post("/translate", json={"text": "Invalid text that causes an error"})
    assert response.status_code == 500
    assert "Internal Server Error" in response.text

def test_translate_russian_to_english():
    response = client.post("/translate", json={"text": "Привет, мир!"})
    assert response.status_code == 200
    assert "translation" in response.json()
    translated_text = response.json()["translation"]
    assert is_english_text(translated_text)

# Вспомогательная функция для проверки, что текст является английским
def is_english_text(text):
    return not any(ord(char) > 127 for char in text)
