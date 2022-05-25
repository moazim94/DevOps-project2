from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app



class TestBase(TestCase):
    def create_app(self):
        return app

class TestDestination(TestBase):
    def test_destination1(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_destination'))
            self.assertIn(b'Austria', response.data)

    def test_destination2(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_destination'))
            self.assertIn(b'Indonesia', response.data)

    def test_destination3(self):
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('get_destination'))
            self.assertIn(b'India', response.data)

    def test_destination4(self):
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('get_destination'))
            self.assertIn(b'U.A.E', response.data)
