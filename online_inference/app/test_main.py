import json
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200

def test_post_bad():
    bad_payload = {'sex': 'b', 'age': '2260', 'chol': '-33.1'}
    r = client.post("/predict/", json.dumps(bad_payload))
    assert r.status_code == 422

def test_post_good_1():
    good_payload = {'sex': 'm', 'age': '60', 'chol': '222'}
    r = client.post("/predict/", json.dumps(good_payload))
    assert r.status_code == 200
    assert r.json()['target'] == '[1]', f"Wrong prediction for {good_payload}"

def test_post_good_0():
    good_payload = {'sex': 'f', 'age': '60', 'chol': '222'}
    r = client.post("/predict/", json.dumps(good_payload))
    assert r.status_code == 200
    assert r.json()['target'] == '[0]', f"Wrong prediction for {good_payload}"

