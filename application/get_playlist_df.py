import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

try:
    with open('../config.json', 'r') as file:
        config_data = json.load(file)
        client_id = config_data['client_id']
        client_secret = config_data['client_secret']
except FileNotFoundError:
    print('Config file not found.')
except json.JSONDecodeError:
    print('Error decoding JSON in the config file.')

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_playlist_df(url):
    playlist_uri = url.split('/')[-1].split('?')[0]

    uri = list()

    for track in sp.playlist_tracks(playlist_uri)['items']:
        uri.append(track['track']['uri'])

    df = pd.DataFrame(uri, columns=['id'])
    df['id'] = df['id'].apply(lambda x: re.findall(r'\w+$', x)[0])

    return df
