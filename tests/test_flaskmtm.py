import pytest
from flaskmtm import create_app


@pytest.fixture()
def app():
    app = create_app("testing")
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


def test_request_index():
    response = client.get("/")
    assert 200 in response.data in response.status_code
