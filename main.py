import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

try:
    with open('config.json', 'r') as file:
        config_data = json.load(file)
except FileNotFoundError:
    print('Config file not found.')
except json.JSONDecodeError:
    print('Error decoding JSON in the config file.')

# Authentication without user
client_credentials_manager = SpotifyClientCredentials(
    client_id=config_data['client_id'], client_secret=config_data['client_secret'])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_link = 'https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f'
playlist_URI = playlist_link.split('/')[-1].split('?')[0]
track_uris = [x['track']['uri']
              for x in sp.playlist_tracks(playlist_URI)['items']]
print(track_uris)
