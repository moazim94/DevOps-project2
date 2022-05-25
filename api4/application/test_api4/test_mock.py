from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_Spring_Austria(self):
        response = self.client.post(url_for('post_review'), data = 'Spring-(Mar-May) Austria')
        self.assertIn(b'The Austrian Alps come to life in the springtime, with wildflowers, green meadows, and dramatic mountains views.', response.data)

    def test_Summer_Austria(self):
        response = self.client.post(url_for('post_review'), data = 'Summer-(Jun-Aug) Austria')
        self.assertIn(b'June-Aug bring beautiful summer weather, particularly the further south you go. Of course the high mountains are always cooler, but with risks of lightning in summer.', response.data)

    def test_Autumn_Austria(self):
        response = self.client.post(url_for('post_review'), data = 'Autumn-(Sep-Nov) Austria')
        self.assertIn(b'Autumn is an excellent time to visit Austria. You can partake in jubilant harvest festivals, see an Almabtrieb cattle procession, drink Sturm (early wine) in cosy Heurigen (wine taverns).', response.data)

    def test_Winter_Austria(self):
        response = self.client.post(url_for('post_review'), data = 'Winter-(Dec-Feb) Austria')
        self.assertIn(b'Christmas and New Year in Austria are magically festive, with gluhwein and Christmas markets everywhere you go, no matter how remote.', response.data)

    def test_Spring_Indonesia(self):
        response = self.client.post(url_for('post_review'), data = 'Spring-(Mar-May) Indonesia')
        self.assertIn(b'Avoid Indonesia in the first month of spring as it is the end of monsoon season. April begins the dry season months.', response.data)
    
    def test_Summer_Indonesia(self):
        response = self.client.post(url_for('post_review'), data = 'Summer-(Jun-Aug) Indonesia')
        self.assertIn(b'Indonesia is now dry and sunny, making it the perfect time to hit popular places like Bali, East Java, Komodo.', response.data)

    def test_Autumun_Indonesia(self):
        response = self.client.post(url_for('post_review'), data = 'Autumn-(Sep-Nov) Indonesia')
        self.assertIn(b'September and October months round up the end of the Indonesian dry season and the Island nation gets prepared for the start of monsoon season in November', response.data)

    def test_Winter_Indonesia(self):
        response = self.client.post(url_for('post_review'), data = 'Winter-(Dec-Feb) Indonesia')
        self.assertIn(b'Indonesia begins and remains in monsoon season until April, not reccomended destination at this time', response.data)

    def test_Spring_India(self):
        response = self.client.post(url_for('post_review'), data = 'Spring-(Mar-May) India')
        self.assertIn(b'India is one of the best countries to visit in March, especially if you want to participate in their colorful Holi Festival.', response.data)

    def test_Summer_India(self):
        response = self.client.post(url_for('post_review'), data = 'Summer-(Jun-Aug) India')
        self.assertIn(b'India, is still in their monsoon season, a good time to avoid as a holiday destination', response.data)

    def test_Autumn_India(self):
        response = self.client.post(url_for('post_review'), data = 'Autumn-(Sep-Nov) India')
        self.assertIn(b'India has finally come out of its long monsoon season. September brings pleasant weather which makes it a good month to visit the country before the winter crowds come.', response.data)

    def test_Winter_India(self):
        response = self.client.post(url_for('post_review'), data = 'Winter-(Dec-Feb) India')
        self.assertIn(b'A winter holiday in India is one of the best experiences one can have. Indulge in skiing, beach fun, water sports, relaxing, festivals, wildlife adventure and other delightful experiences during winters in India.', response.data)

    def test_Spring_UAE(self):
        response = self.client.post(url_for('post_review'), data = 'Spring-(Mar-May) U.A.E')
        self.assertIn(b'During this time of year, there is a perfect balance as the days are starting to become hotter and last longer, while nighttime temperatures are dropping so be sure to take along a light jacket for the evening.', response.data)

    def test_Summer_UAE(self):
        response = self.client.post(url_for('post_review'), data = 'Summer-(Jun-Aug) U.A.E')
        self.assertIn(b'Dubai will experience an average of 10-12 hours of daylight and will need to seek shade during the main part of the day, when temperatures are extremely hot, best to avoid if not use to extreme temperatures.', response.data)
    
    def test_Autumn_UAE(self):
        response = self.client.post(url_for('post_review'), data = 'Autumn-(Sep-Nov) U.A.E')
        self.assertIn(b'during these months, you can bask in the warmth of the United Arab Emirates desert-like climate and avoid the peak of the heat.', response.data)

    def test_Winter_UAE(self):
        response = self.client.post(url_for('post_review'), data = 'Winter-(Dec-Feb) U.A.E')
        self.assertIn(b'The coolest month of the year for Dubai is January, where the average daytime high is 24 degrees. The average overnight low in January is 14 degrees and the average sea temperature of Dubai in January is 23 degrees. A perfect sunny Christmas break.', response.data)
