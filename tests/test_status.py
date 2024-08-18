from unittest import TestCase

from fastapi.testclient import TestClient
from task_manager.main import app
from task_manager.settings import settings


class TestPing(TestCase):
    def test_status(self):
        client = TestClient(app)
        result = client.get(settings.status_url)
        assert result.status_code == 200
        assert result.json() == {"status": "ok"}
