import pandas as pd

df = pd.read_csv('./data/processed_data.csv')

test_playlist = df[df['name'] == 'lit']
test_playlist.reset_index(drop=True, inplace=True)

print(test_playlist.shape)

with open('./data/test_playlist.csv', 'w') as file:
    pass

test_playlist.to_csv('./data/test_playlist.csv')
