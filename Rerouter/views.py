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
        return utils.ConfigureResponse(response)

    if request.method == "POST":
        if(utils.ItIsSlack(request)):
            # convert request body to a dictionary
            request_as_a_dict = yaml.safe_load(request.body.decode("utf-8"))
            # If the request has the event field, handle the event
            if 'event' in request_as_a_dict:
                event = request_as_a_dict['event']
                utils.Handle(event)
            else:
                response = Response('Event missing!')
                return utils.ConfigureResponse(response)
        else:
            response = Response('Fuck Off, stay away from my API!')
            return utils.ConfigureResponse(response)

        response = Response(request)
        return utils.ConfigureResponse(response)
