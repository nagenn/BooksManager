#Simple test of the app
import requests

def test_login():
    r = requests.post(
        "http://localhost:8383/login",
        data={"username":"admin","password":"admin"}
    )
    assert r.status_code == 200
