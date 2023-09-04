import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

tracks = pd.read_csv('../data/tracks.csv')
feature_set = pd.read_csv('../data/feature_set.csv')


def get_playlist_vector(feature_set, playlist_df):
    '''
    Summarize a user's playlist into a vector.
    '''
    feature_set_playlist = feature_set[feature_set['id'].isin(playlist_df)]
    feature_set_playlist.drop(columns='id', inplace=True)
    playlist_vector = feature_set_playlist.sum()

    feature_set_nonplaylist = feature_set[~feature_set['id'].isin(playlist_df)]

    return playlist_vector, feature_set_nonplaylist


def get_recommendations(tracks, playlist_vector, feature_set_nonplaylist, n=10):
    '''
    Generate music recommendations.
    '''
    nonplaylist_tracks = tracks[tracks['id'].isin(
        feature_set_nonplaylist['id'].values)]

    # calculate cosine similarity between the playlist and each non-playlist track
    nonplaylist_tracks['similarity'] = cosine_similarity(feature_set_nonplaylist.drop(
        'id', axis=1).values, playlist_vector.values.reshape(1, -1))[:, 0]

    return nonplaylist_tracks.sort_values('similarity', ascending=False).head(n)
