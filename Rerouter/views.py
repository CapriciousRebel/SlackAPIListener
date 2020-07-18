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
# App imports
from . import utils


@csrf_exempt
def rerouter(request):

    if request.method == "GET":
        print(request.headers)
        content = "Hello! Make a POST Requests on this url with auth token from your slack app to access the services."
        response = Response(content)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response

    if request.method == "POST":

        print(request.headers)

        response = Response(content)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
