from app import app as flask_app
import pytest

@pytest.fixture
def app():
    return flask_app

def test_get_articles(client):
    response = client.get('/blog/no-articles')
    assert response.status_code == 404