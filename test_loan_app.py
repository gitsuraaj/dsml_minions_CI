import pytest
from loan_app import app

@pytest.fixture
def client():
    return app.test_client()


def test_ping(client):
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json == { 'Pinging the model successful' : 'Hurray' }


def test_predict (client):
    test_json={
        "Gender": "Male",
        "Married": "Unmarried",
        "ApplicantIncome": 50000,
        "Credit_History": 1.0,
        "LoanAmount": 500000
    }

    resp = client.post("/predict", json= test_json)
    assert resp.status_code == 500
    assert resp.json == {"loan_approval_status: ": "Rejected"}


