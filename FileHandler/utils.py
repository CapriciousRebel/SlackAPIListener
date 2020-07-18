import os


# Fetch the config vars
GOOGLE_DRIVE_BEARER_TOKEN = os.environ.get('GOOGLE_DRIVE_BEARER_TOKEN')
SLACK_APP_BEARER_TOKEN = os.environ.get('SLACK_APP_BEARER_TOKEN')
DRIVE_FOLDER_ID = os.environ.get('DRIVE_FOLDER_ID')
TEMP_FILE = '/tmp/temp.jpg'


# Save the file from Slack file storage to /tmp/temp.jpg
def save_to_tmp(image_url):
    try:
        headers = {"Authorization": f"Bearer {SLACK_APP_BEARER_TOKEN}"}
        img_data = requests.get(
            image_url, headers=headers).content
    except:
        print("Failed to get the file from slack!!!")
        return 0
    try:
        with open(TEMP_FILE, 'wb') as handler:
            handler.write(img_data)
        return 1
    except:
        print("Failed to write the file in /tmp/!")
        return 0


# Upload file from /tmp/temp.jpg to google drive
def upload_to_drive(file_name):
    try:
        headers = {"Authorization": f"Bearer {GOOGLE_DRIVE_BEARER_TOKEN}"}
        para = {
            "name": file_name,
            "parents": [DRIVE_FOLDER_ID]
        }

        files = {
            'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
            'file': ('image/jpeg', open(TEMP_FILE, "rb"))
        }

        response = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files
        )
        return 1
    except:
        return 0


# delete file from /tmp/temp.jpg
def delete_from_tmp():
    os.remove(TEMP_FILE)
    return 1
