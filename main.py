import spotipy
import json
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

try:
    with open('config.json', 'r') as file:
        config_data = json.load(file)
except FileNotFoundError:
    print('Config file not found.')
except json.JSONDecodeError:
    print('Error decoding JSON in the config file.')

columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
           'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']

track_data = pd.DataFrame(columns=columns)

# authentication without user
client_credentials_manager = SpotifyClientCredentials(
    client_id=config_data['client_id'], client_secret=config_data['client_secret'])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_link = 'https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f'
playlist_URI = playlist_link.split('/')[-1].split('?')[0]

for track in sp.playlist_tracks(playlist_URI)['items']:
    track_uri = track['track']['uri']

    track_features = pd.DataFrame(
        [sp.audio_features(track_uri)[0]], columns=columns)

    track_data = pd.concat([track_data, track_features], ignore_index=True)

print(track_data.head())
