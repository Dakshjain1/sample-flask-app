import json
from api import app as flask_app
import pytest


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    assert b"Hello daksh jain" in res.data


