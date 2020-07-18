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

        body = request.get_data()

        XSlackRequestTimestamp = request.headers['X-Slack-Request-Timestamp']

        sig_basestring = 'v0:%s:%s' % (timestamp, body.decode('utf-8'))
        computed_sha = hmac.new(secret,
                                sig_basestring.encode('utf-8'),
                                digestmod=hashlib.sha256).hexdigest()
        my_sig = 'v0=%s' % (computed_sha,)

        slack_sig = request.headers['X-Slack-Signature']
        print(slack_sig == my_sig)

        response = Response(request)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
