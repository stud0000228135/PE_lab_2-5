from fastapi.testclient import TestClient
from FastAPI import app

client = TestClient(app)

def test_translate_endpoint():
    response = client.post("/translate", json={"text": "Привет, мир!"})
    assert response.status_code == 200
    assert response.json() == {'translation': 'Hey, world!'}
