# tests/test_api.py
from fastapi.testclient import TestClient
from datetime import datetime, timedelta
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "Test Description",
            "priority": 3,
            "due_date": (datetime.now() + timedelta(days=1)).isoformat()
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["priority"] == 3

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_filter_tasks():
    # Create a task with priority 1
    client.post(
        "/tasks/",
        json={
            "title": "Priority 1 Task",
            "priority": 1,
            "description": "Test"
        }
    )
    
    # Filter tasks by priority
    response = client.get("/tasks/?priority=1")
    assert response.status_code == 200
    tasks = response.json()
    assert all(task["priority"] == 1 for task in tasks)