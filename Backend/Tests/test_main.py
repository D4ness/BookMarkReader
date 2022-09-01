from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main_200():
    response = client.get("/")
    assert response.status_code == 200


def test_book_is_achievable_after_creating():
    file_name = 'example_for_testing.txt'
    with open(f"TestFileSource/{file_name}", "rb") as f:
        response_on_creat = client.post("/books", files={"files": (file_name, f)})
    assert response_on_creat.status_code == 200
    created = response_on_creat.json()
    response = client.get(f"/books/{created['id']}")
    assert response.status_code == 200
    got = response.json()
    assert got['id'] == created['id']