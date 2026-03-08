# tests/test_tasks_api.py


def test_get_tasks_returns_task_list(client):
    response = client.get("/tasks")

    assert response.status_code == 200

    # Convert JSON response body into a Python object
    data = response.get_json()

    assert isinstance(data, list)


def test_get_existing_task_returns_task(client):
    response = client.get("/tasks/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1


def test_get_missing_task_returns_404(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404


def test_create_task_returns_201(client):
    response = client.post(
        "/tasks",
        # json= sends a JSON request body and sets the correct header
        json={"title": "Write integration tests"}
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Write integration tests"


def test_create_task_missing_title_returns_400(client):
    response = client.post(
        "/tasks",
        json={}
    )

    assert response.status_code == 400


def test_update_existing_task_returns_updated_task(client):
    response = client.put(
        "/tasks/1",
        json={"title": "Updated task"}
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["title"] == "Updated task"


def test_update_missing_task_returns_404(client):
    response = client.put(
        "/tasks/999",
        json={"title": "Updated task"}
    )

    assert response.status_code == 404


def test_update_task_missing_title_returns_400(client):
    response = client.put(
        "/tasks/1",
        json={}
    )

    assert response.status_code == 400


def test_delete_existing_task_returns_204(client):
    response = client.delete("/tasks/1")

    # 204 indicates success but returns no response body
    assert response.status_code == 204


def test_delete_missing_task_returns_404(client):
    response = client.delete("/tasks/999")

    assert response.status_code == 404