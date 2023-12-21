import pytest
from fastapi.testclient import TestClient
from FastAPI import app

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
    assert contains_russian_letters(translated_text)

def contains_russian_letters(text):
    # Является ли символ кириллическим
    def is_cyrillic(char):
        return 'а' <= char.lower() <= 'я' or char.lower() == 'ё'
    
    # Проверяем, содержит ли текст хотя бы одну русскую букву
    return any(is_cyrillic(char) for char in text)

