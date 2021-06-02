import json
import os

from djangoProject.settings import BASE_DIR


class TwitterAPIUtil:

    @staticmethod
    def postStatus(tweetJson):
        return True

    @staticmethod
    def getTweetsFromTwitter(configurations):
 #       response = "sample"
  #      print(configurations)
   #     return response
        json_data = os.path.join(BASE_DIR, 'static', "SampleResponse.json")
        fileData = open(json_data, 'r')
        response = json.load(fileData)
        fileData.close()
        return response

