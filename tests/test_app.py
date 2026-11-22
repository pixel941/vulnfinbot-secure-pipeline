import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_chat_success(client):
    response = client.post(
        "/api/chat",
        json={"message": "Hello"}
    )
    assert response.status_code == 200
    assert "response" in response.json


def test_chat_missing_message(client):
    response = client.post("/api/chat", json={})
    assert response.status_code == 400


def test_chat_empty_message(client):
    response = client.post(
        "/api/chat",
        json={"message": "   "}
    )
    assert response.status_code == 400


def test_chat_invalid_type(client):
    response = client.post(
        "/api/chat",
        json={"message": 123}
    )
    assert response.status_code == 400


def test_chat_too_long(client):
    response = client.post(
        "/api/chat",
        json={"message": "A" * 1001}
    )
    assert response.status_code == 400


def test_chat_invalid_content_type(client):
    response = client.post(
        "/api/chat",
        data="Hello",
        content_type="text/plain"
    )
    assert response.status_code == 415