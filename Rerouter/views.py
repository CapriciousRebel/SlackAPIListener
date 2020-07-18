# Django imports
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# DRF imports
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
# Python imports
import yaml
import json
import requests
import os
import hmac
import hashlib
# App imports

# Config Vars
SLACK_APP_SIGNING_SECRET = os.environ.get('SLACK_APP_SIGNING_SECRET')


@csrf_exempt
def rerouter(request):

    if request.method == "GET":
        content = "Hello! Make a POST Requests on this url with auth token from your slack app to access the services."
        response = Response(content)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response

    if request.method == "POST":

        Body = request.body.decode('utf-8')
        XSlackRequestTimestamp = request.headers['X-Slack-Request-Timestamp']
        XSlacksignature = request.headers['X-Slack-Signature']
        Headers = request.headers

        BaseSign = 'v0:%s:%s' % (XSlackRequestTimestamp, Body)
        ComputedSHA = hmac.new(bytes(SLACK_APP_SIGNING_SECRET, 'utf-8'),
                               BaseSign.encode('utf-8'),
                               digestmod=hashlib.sha256).hexdigest()

        XAppSignature = 'v0=%s' % (ComputedSHA,)

        print(XAppSignature)
        print(XSlacksignature)

        response = Response(request)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
