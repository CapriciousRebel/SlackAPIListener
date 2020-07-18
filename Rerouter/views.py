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
from Rerouter import utils


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
        
        if(utils.ItIsSlack(request)):
            print("Verified!")
        else:
            response = Response('Fuck Off, stay away from my API!')
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            return response

        response = Response(request)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
