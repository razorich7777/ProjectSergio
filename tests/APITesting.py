import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post():
    response = requests.get(f"{BASE_URL}/comments/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data
    assert "email" in data
    print(data["body"])
    print(data["email"])

def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "foo"
    assert data["body"] == "bar"
    assert data["userId"] == 1
