import os

from django.template import loader

from django.http import HttpResponse
import json

# Create your views here.
from djangoProject.settings import BASE_DIR
from twitterClient.APIUtil.TwitterAPIUtil import TwitterAPIUtil
from twitterClient.constants import APIConstants
from twitterClient.properties.Singleton import Singleton


def index(request):
    template = loader.get_template('index.html')
    data_json = Singleton.getConfigurations()
    response = TwitterAPIUtil.getTweetsFromTwitter(data_json)
    data = response[APIConstants.data]
    metaData = response[APIConstants.meta]
    nextToken = metaData[APIConstants.nextToken]
    if APIConstants.prev_token == '':
        APIConstants.prevToken = nextToken
    context = {
        'data': data,
        'nextToken': nextToken,
        'prevToken': APIConstants.prevToken,
        'newestId': metaData[APIConstants.newestId],
        'oldestId': metaData[APIConstants.oldestId]

    }
    return HttpResponse(template.render(context, request))


#need to update with twitter response
def nextPage(request, next_token):
    template = loader.get_template('index.html')
    data_json = Singleton.getConfigurations()
    #get new response with next_token
    response = TwitterAPIUtil.getTweetsFromTwitter(data_json)
    data = response[APIConstants.data]
    metaData = response[APIConstants.meta]
    nextToken = metaData[APIConstants.nextToken]
    if APIConstants.prev_token == '':
        APIConstants.prevToken = nextToken
    context = {
        'data': data,
        'nextToken': nextToken,
        'prevToken': APIConstants.prevToken,
        'newestId': metaData[APIConstants.newestId],
        'oldestId': metaData[APIConstants.oldestId],
        'newPage' : True

    }
    return HttpResponse(template.render(context, request))
    #    return HttpResponse("<h1> Simple web app <h1>")


def postTweet(request, content):
    # tweet json creation
    tweetJSON = content
    TwitterAPIUtil.postStatus(tweetJSON)
    context = {
        'status': 'success',
    }
    template = loader.get_template('tweetStatus.html')
    return HttpResponse(template.render(context, request))
