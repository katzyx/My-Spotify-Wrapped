import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import base64
from requests import post
import json
from flask import Flask, redirect, request
import urllib.parse

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
ACCESS_TOKEN = "https://accounts.spotify.com/authorize?response_type=code&client_id=84b6f9b3a8b345ac9497f330d9f3a52f&scope=playlist-modify-private&redirect_uri=https://www.google.ca/"

app = Flask(__name__)
redirect_uri = 'https://www.google.ca/'

# define /login route  
@app.route('/login')
def login():
    '''build authorization url and send GET request to /authorize'''

    print("Redirect to Spotify Login Page")
    scope = "playlist-read-private playlist-read-collaborative user-top-read user-read-recently-played user-library-read playlist-read-collaborative"

    # create query parameters
    q_params = {'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': scope,
        'redirect_uri': redirect_uri}
    
    auth_url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(q_params)
    
    return redirect(auth_url)


def get_genre(id):
    '''get the genres that are associated with an artist'''
    track_url = "https://api.spotify.com/v1/tracks/" + id
    headers = {"Authorization": f"Bearer " + ACCESS_TOKEN}
    response = requests.get(track_url, headers)
    
    print(track_url)
    print(headers)
    print(response)
    return


if __name__ == "__main__":
    # app.run(host="localhost", port=5000)
    get_genre("2ccc2493302d46e8")


