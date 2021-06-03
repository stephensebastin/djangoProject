import json
import os

from djangoProject.settings import BASE_DIR


class TwitterAPIUtil:

    @staticmethod
    def postStatus(tweetJson):
        """curl - XPOST
        --url
        'https://api.twitter.com/1.1/statuses/update.json?status=hello'
        --header
        'authorization: OAuth
        oauth_consumer_key = "oauth_customer_key",
        oauth_nonce = "generated_oauth_nonce",
        oauth_signature = "generated_oauth_signature",
        oauth_signature_method = "HMAC-SHA1",
        oauth_timestamp = "generated_timestamp",
        oauth_token = "oauth_token",
        oauth_version = "1.0"' """
        return True

    @staticmethod
    def getTweetsFromTwitter(configurations):
 #       response = "sample"
  #      print(configurations)
   #     return response
        #https://api.twitter.com/2/users/2244994945/tweets?tweet.fields=created_at&max_results=100&start_time=2019-01-01T17:00:00Z&end_time=2020-12-12T01:00:00Z
        json_data = os.path.join(BASE_DIR, 'static', "SampleResponse.json")
        fileData = open(json_data, 'r')
        response = json.load(fileData)
        fileData.close()
        return response

