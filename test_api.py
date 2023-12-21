def test_translate_english_to_russian():
    # Отправляем текст на английском для перевода
    response = client.post("/translate", json={"text": "Hello, world!"})
    
    # Проверяем успешный код состояния
    assert response.status_code == 200
    
    # Получаем переведенный текст из ответа
    translated_text = response.json()["translation"]
    
    # Проверяем, что результат не пустой и отличается от исходного текста
    assert translated_text
    assert translated_text != "Hello, world!"
