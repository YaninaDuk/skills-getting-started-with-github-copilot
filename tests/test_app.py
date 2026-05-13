import pytest
from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Add more tests for signup, unregister, and edge cases
