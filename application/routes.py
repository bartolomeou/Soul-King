import pandas as pd
from flask import Flask, render_template, request
from get_playlist_df import get_playlist_df
from content_based_recsys import get_recommendations

tracks = pd.read_csv('../data/tracks.csv')
feature_set = pd.read_csv('../data/feature_set.csv')

app = Flask(__name__)


@app.route('/')
def hone():
    # return "<p>Hello, World!</p>"
    return render_template('home.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    url = request.form['URL']
    playlist_df = get_playlist_df(url)

    num_recommendations = int(request.form['number-of-recs'])

    recommendations = get_recommendations(playlist_df, num_recommendations)
    recommendations.reset_index(drop=True, inplace=True)

    print(recommendations)

    tracks = []
    for i in range(num_recommendations):
        tracks.append(recommendations.at[i, 'track_name'] +
                      ' - ' + recommendations.at[i, 'artist_name'])

    return render_template('results.html', songs=tracks)
