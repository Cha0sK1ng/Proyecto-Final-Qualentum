import os
import pytest

os.environ["DATABASE_URI"] = "sqlite:///:memory:"

from app import create_app, db

@pytest.fixture
def app():
    app = create_app("development")
    app.config["TESTING"] = True
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()