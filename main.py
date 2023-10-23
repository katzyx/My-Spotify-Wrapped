import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import base64
from requests import post
import json

# --- CLIENT CREDITAILS --- #
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    ''' get authorization token'''

    # create auth string, encode with base64
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")

    # convert base64 object to string to pass with header
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    # url to send request to /api/token endpoint of spotify oauth
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    # send auth request, returns json data in .content field
    result = post(url, headers=headers, data=data)

    # convert json data (string) to python dictionary to access the data
    json_result = json.loads(result.content)
    token = json_result["access_token"]

    return token

def get_auth_header(token):
    '''construct header when sending request'''
    return {"Authorization": "Bearer " + token}

# --- END CLIENT CREDENTIALS --- #




token = get_token()