import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_translate_english_to_russian():
    # Отправляем текст на английском для перевода
    response = client.post("/translate", json={"text": "Hello, world!"})
    
    # Проверяем успешный код состояния
    assert response.status_code == 200
    
    # Получаем переведенный текст из ответа
    translated_text = response.json()["translation"]
    
    # Проверяем, что результат не пустой и содержит русские буквы
    assert translated_text
    assert not contains_english_letters(translated_text)

def contains_english_letters(text):
    # Проверяем, содержит ли текст хотя бы одну английскую букву
    return any('a' <= char.lower() <= 'z' for char in text)

