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

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

app = Flask(__name__)
redirect_uri = 'http://localhost:8888/callback'

# define /login route  
@app.route('/login')
def login():
    '''build authorization url and send GET request to /authorize'''

    print("Redirect to Spotify Login Page")
    scope = "playlist-read-private playlist-read-collaborative user-top-read user-read-recently-played user-library-read playlist-read-collaborative"

    # create query parameters
    q_params = {'response_type': 'code',
        'client_id': client_id,
        'scope': scope,
        'redirect_uri': redirect_uri}
    
    auth_url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(q_params)
    
    return redirect(auth_url)

if __name__ == "__main__":
    app.run(host="localhost", port=5000)


