import pytest

from backend import create_app
from yr_filter.yr_filter import YrFilter


@pytest.fixture()
def test_client():
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    app = create_app()
    testing_client = app.test_client()
    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.fixture()
def yr_filter() -> YrFilter:
    return YrFilter()
