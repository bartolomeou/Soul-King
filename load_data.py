from pprint import pprint
import json
import pandas as pd

'''
Transform raw json data to a csv file.
'''


# import json
path = './data/challenge_set.json'
raw_json = json.loads(open(path).read())

# transform data
playlists = raw_json["playlists"]
df = pd.json_normalize(playlists, record_path='tracks',
                       meta=['name'], errors='ignore')

# output
df.to_csv('./data/raw_data.csv')
