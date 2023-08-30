import pandas as pd

df = pd.read_csv('./data/processed_data.csv')

test_playlist = df[df['name'] == 'Throwbacks']

with open('./data/test_playlist.csv', 'w') as file:
    pass

test_playlist.to_csv('./data/test_playlist.csv')
