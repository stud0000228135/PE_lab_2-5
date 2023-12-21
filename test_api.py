import json
from fastapi.testclient import TestClient
from FastAPI import app 

client = TestClient(app)

def test_translate_success():
    response = client.post("/translate", json={"text": "Hello, world!"})
    assert response.status_code == 200
    assert "translation" in response.json()

def test_translate_error():
    response = client.post("/translate", json={"text": "Invalid text that causes an error"})
    assert response.status_code == 500
