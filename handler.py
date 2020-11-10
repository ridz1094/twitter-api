import json
import tweepy
import tweet_auth

def postTweet(event, context):
    statusCode = 200
    result = {}
    try:
        result = tweet_auth.get_api().update_status(event["message"])
    except tweepy.TweepError as e:
        statusCode = 400
        result = handle_exception(e)

    response = {
        "statusCode": statusCode,
        "result": result
    }

    return response


def displayTweet(event, context):
    statusCode = 200
    result = {}
    try:
        result = tweet_auth.get_api().user_timeline(count=100)
    except tweepy.TweepError as e:
        statusCode = 400
        result = handle_exception(e)

    response = {
        "statusCode": statusCode,
        "result": result
    }

    return response


def deleteTweet(event, context):
    statusCode = 200
    result = {}
    try:
        result = tweet_auth.get_api().destroy_status(event["id"])
    except tweepy.TweepError as e:
        statusCode = 400
        result = handle_exception(e)
    response = {
        "statusCode": statusCode,
        "result": result
    }
    return response


def searchTweet(event, context):
    statusCode = 200
    result = {}
    try:
        result = tweet_auth.get_api().user_timeline(event["keyword"])
    except tweepy.TweepError as e:
        statusCode = 400
        result = handle_exception(e)
    response = {
        "statusCode": statusCode,
        "result": result
    }
    return response

def handle_exception(e):
    return e.response.text
