import requests 
import os 

CLIENT_ID = "dfcb8efca0ad42a8ba491e4317d7984e"
CLIENT_SECRET = "ee51627386e5402fbd26c9b85bdce936"

CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'


auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()
access_token = auth_response_data.get('access_token')


headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
query = input("Enter search term: ")

response = requests.get(BASE_URL + 'search/?q=' + query + '&type=track' , headers=headers)
tracks = response.json().get("tracks", {}).get("items", [])

track_id = input('Enter track id: ')

track_names = [track["name"] for track in tracks]





