# Python imports
import requests
import hashlib
import json
import hmac
import os


# Config Vars
SLACK_APP_SIGNING_SECRET = os.environ.get('SLACK_APP_SIGNING_SECRET')

# Returns True if it is slack


def ItIsSlack(request):
    # Fetch the headers and body
    Headers = request.headers
    Body = request.body.decode('utf-8')

    # Fetch the Slack header values
    XSlackRequestTimestamp = Headers['X-Slack-Request-Timestamp']
    XSlacksignature = Headers['X-Slack-Signature']

    # Compute the Signature
    BaseSign = 'v0:%s:%s' % (XSlackRequestTimestamp, Body)
    ComputedSHA = hmac.new(bytes(SLACK_APP_SIGNING_SECRET, 'utf-8'),
                           BaseSign.encode('utf-8'),
                           digestmod=hashlib.sha256).hexdigest()
    XAppSignature = 'v0=%s' % (ComputedSHA,)

    # Compare the Signature
    return True if XAppSignature == XSlacksignature else False


def ConfigureResponse(response):
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = "application/json"
    response.renderer_context = {}
    return response


def Handle(event):
    if "files" in event:
        requests.post(
            "https://slack-api-listener.herokuapp.com/FileHandler/drive_backup",
            event=event)
