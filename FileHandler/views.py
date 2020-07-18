# Django imports
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# DRF imports
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
# Python imports
import yaml
import json
import requests
import os
# App imports
from . import utils


# Fetch the config vars
SLACK_APP_BEARER_TOKEN = os.environ.get('SLACK_APP_BEARER_TOKEN')
DRIVE_FOLDER_ID = os.environ.get('DRIVE_FOLDER_ID')
GOOGLE_DRIVE_BEARER_TOKEN = os.environ.get('GOOGLE_DRIVE_BEARER_TOKEN')
TEMP_FILE = '/tmp/temp.jpg'


@csrf_exempt
def drive_backup(request):

    if request.method == "GET":
        content = "Hello! Make a POST Request here to store the files to drive from slack."
        response = Response(content)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response

    if request.method == "POST":
        try:
            # convert request body to a dictionary
            request_as_a_dict = yaml.safe_load(request.body.decode("utf-8"))

            if "event" in request_as_a_dict:

                # fetch the files uploaded
                file_as_a_dict = request_as_a_dict['event']

                if "files" in file_as_a_dict:
                    # store each file in /tmp/temp.jpg and then upload to drive
                    for i in range(len(file_as_a_dict['files'])):
                        image_url = file_as_a_dict['files'][i]['url_private_download']
                        utils.save_to_tmp(image_url)
                        utils.upload_to_drive("Filename")
                        utils.delete_from_tmp()
        except:
            # Send the request as a response when slack first talk to the API with challenge parameter
            response = Response(request)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            return response
        finally:
            # Send the request as a response when slack first talk to the API with challenge parameter
            response = Response(request)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            return response
