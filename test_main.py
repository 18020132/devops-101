from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_result():
    response = client.post("/", json={"number_1": 10, "number_2": 2})
    print(response.status_code)
    print(response.content)
    assert response.json() == {"result": 5.0}

def test_zero():
    response = client.post("/", json={"number_1": 10, "number_2": 0})
    print(response.status_code)
    assert response.json() == {"result": "error"}

# def test_valid_1():
#     response = client.post("/", json={"number_1": 10, "number_2": "a"})
#     assert response.json() == {"result": "error"}

# def test_valid_2():
#     response = client.post("/", json={"number_1": "a", "number_2": 2})
#     assert response.json() == {"result": "error"}

test_result()