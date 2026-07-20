import unittest

from fastapi.testclient import TestClient

from backend.main import app


class PlatformFoundationTest(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health_endpoint_returns_platform_status(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["status"], "healthy")
        self.assertEqual(payload["database"], "connected")
        self.assertEqual(payload["plugins"], 0)
        self.assertEqual(payload["version"], "0.1.0")

    def test_plugins_endpoint_returns_empty_registry(self):
        response = self.client.get("/plugins")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])


if __name__ == "__main__":
    unittest.main()
