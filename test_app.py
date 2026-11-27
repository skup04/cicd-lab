# test_app.py
import unittest

from app import health


class HealthTest(unittest.TestCase):
    def test_health_reports_ok(self):
        self.assertEqual(health(), {"status": "ok"})
