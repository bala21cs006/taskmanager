import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.database import get_db, Base

# Use in-memory SQLite for tests
TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


# ── Fixtures ──────────────────────────────────────────────────
@pytest.fixture(autouse=True)
def clean_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield


def register_and_login(email="test@test.com", password="secret123"):
    client.post("/register", json={"email": email, "password": password})
    res = client.post("/login", json={"email": email, "password": password})
    return res.json()["access_token"]


# ── Auth Tests ─────────────────────────────────────────────────
def test_register():
    res = client.post("/register", json={"email": "bala@test.com", "password": "pass123"})
    assert res.status_code == 201
    assert res.json()["email"] == "bala@test.com"


def test_register_duplicate_email():
    client.post("/register", json={"email": "bala@test.com", "password": "pass123"})
    res = client.post("/register", json={"email": "bala@test.com", "password": "pass456"})
    assert res.status_code == 400


def test_login_success():
    client.post("/register", json={"email": "bala@test.com", "password": "pass123"})
    res = client.post("/login", json={"email": "bala@test.com", "password": "pass123"})
    assert res.status_code == 200
    assert "access_token" in res.json()


def test_login_wrong_password():
    client.post("/register", json={"email": "bala@test.com", "password": "pass123"})
    res = client.post("/login", json={"email": "bala@test.com", "password": "wrongpass"})
    assert res.status_code == 401


# ── Task Tests ─────────────────────────────────────────────────
def test_create_task():
    token = register_and_login()
    res = client.post("/tasks", json={"title": "Buy groceries", "description": "Milk, eggs"}, headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 201
    assert res.json()["title"] == "Buy groceries"
    assert res.json()["completed"] is False


def test_get_tasks():
    token = register_and_login()
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/tasks", json={"title": "Task 1"}, headers=headers)
    client.post("/tasks", json={"title": "Task 2"}, headers=headers)
    res = client.get("/tasks", headers=headers)
    assert res.status_code == 200
    assert res.json()["total"] == 2


def test_get_task_by_id():
    token = register_and_login()
    headers = {"Authorization": f"Bearer {token}"}
    task = client.post("/tasks", json={"title": "My task"}, headers=headers).json()
    res = client.get(f"/tasks/{task['id']}", headers=headers)
    assert res.status_code == 200
    assert res.json()["title"] == "My task"


def test_mark_task_completed():
    token = register_and_login()
    headers = {"Authorization": f"Bearer {token}"}
    task = client.post("/tasks", json={"title": "Do laundry"}, headers=headers).json()
    res = client.put(f"/tasks/{task['id']}", json={"completed": True}, headers=headers)
    assert res.status_code == 200
    assert res.json()["completed"] is True


def test_delete_task():
    token = register_and_login()
    headers = {"Authorization": f"Bearer {token}"}
    task = client.post("/tasks", json={"title": "Temp task"}, headers=headers).json()
    res = client.delete(f"/tasks/{task['id']}", headers=headers)
    assert res.status_code == 204


def test_filter_completed_tasks():
    token = register_and_login()
    headers = {"Authorization": f"Bearer {token}"}
    t1 = client.post("/tasks", json={"title": "Task A"}, headers=headers).json()
    client.post("/tasks", json={"title": "Task B"}, headers=headers)
    client.put(f"/tasks/{t1['id']}", json={"completed": True}, headers=headers)
    res = client.get("/tasks?completed=true", headers=headers)
    assert res.json()["total"] == 1


def test_cannot_access_other_users_task():
    token1 = register_and_login("user1", "u1@test.com", "pass")
    token2 = register_and_login("user2", "u2@test.com", "pass")
    task = client.post("/tasks", json={"title": "Private"}, headers={"Authorization": f"Bearer {token1}"}).json()
    res = client.get(f"/tasks/{task['id']}", headers={"Authorization": f"Bearer {token2}"})
    assert res.status_code == 404


def test_unauthorized_access():
    res = client.get("/tasks")
    assert res.status_code == 401
