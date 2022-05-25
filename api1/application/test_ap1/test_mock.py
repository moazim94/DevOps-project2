from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestSuggestion(TestBase):
    def test_Seasonal_Holidays(self):
        with patch("requests.get") as g:
            with patch("requests.post") as p:
                g.return_value.text = "Spring-(Mar-May),Austria"
                p.return_value.text = "The Austrian Alps come to life in the springtime, with wildflowers, green meadows, and dramatic mountains views."
                response = self.client.get(url_for('get_recommended_holiday'))
                self.assertIn(b'Spring-(Mar-May),Austria', response.data)
                self.assertIn(b'The Austrian Alps come to life in the springtime, with wildflowers, green meadows, and dramatic mountains views.', response.data)