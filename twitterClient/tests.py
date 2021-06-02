from django.test import TestCase

from twitterClient.APIUtil.TwitterAPIUtil import TwitterAPIUtil
from twitterClient.models import models

# Create your tests here.
class TestCases(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_nextPage(self):
        response = self.client.get('/dsda43')
        self.assertEqual(response.status_code, 200)

    def test_PostStatus(self):
        tweetJson = {"tweetData":"Sample Tweet"}
        if TwitterAPIUtil.postStatus(tweetJson):
            print('PASS')
    #dummy test cases
    def test_getTweetsFromTwitter(self):
        configurations = {"api_key": "yyyyyy", "client_secret":"zxxxxx"}
        response = TwitterAPIUtil.getTweetsFromTwitter(configurations)
        if response is not '':
            print('PASS')