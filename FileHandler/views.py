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
def drive_backup(request):
    if request.method == "POST":
        
        print("POST Request made!")
        
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
                        # Save File from Slack API to /tmp/

                        if(utils.save_to_tmp(image_url)):
                            if(utils.upload_to_drive("Filename")):
                                utils.delete_from_tmp()
                            else:
                                return Response("Failed to Get the file from Slack, try changing the SLACK_APP_BEARER_TOKEN, or add files:read scope to it.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        else:
                            return Response("Failed to Upload the file to drive, try changing the GOOGLE_DRIVE_BEARER_TOKEN, or check it's scopes. Also Check the DRIVE_FOLDER_ID", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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
