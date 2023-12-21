import pytest
from httpx import AsyncClient
from FastAPI import app

client = TestClient(app)

def test_health_check():
    response = client.get("/translate")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

