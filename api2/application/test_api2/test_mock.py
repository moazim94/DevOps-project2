from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app



class TestBase(TestCase):
    def create_app(self):
        return app

class TestSeason(TestBase):
    def test_season1(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_season'))
            self.assertIn(b'Spring-(Mar-May)', response.data)
    
    def test_season2(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_season'))
            self.assertIn(b'Summer-(Jun-Aug)', response.data)

    def test_season3(self):
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('get_season'))
            self.assertIn(b'Autumn-(Sep-Nov)', response.data)


    def test_season4(self):
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('get_season'))
            self.assertIn(b'Winter-(Dec-Feb)', response.data)

 