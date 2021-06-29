import requests


url = "http://127.0.0.1:5000"


def test_index_page():
    r = requests.get(url + "/")
    assert r.status_code == 404


def test_get_all_notes():
    r = requests.get(url + "/api/note")
    assert r.status_code == 200
