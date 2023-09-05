import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

tracks = pd.read_csv('../data/tracks.csv')
feature_set = pd.read_csv('../data/feature_set.csv')


def _get_playlist_vector(playlist_df):
    '''
    Summarize a user's playlist into a vector.
    '''
    # filter feature_set to only include tracks in the playlist
    feature_set_playlist = feature_set[feature_set['id'].isin(playlist_df)]

    # number of tracks in the playlist that were not found in feature_set
    not_included = playlist_df.shape[0] - feature_set_playlist.shape[0]
    print('Could not find {} tracks.'.format(not_included))

    feature_set_playlist.drop(columns='id', inplace=True)

    playlist_vector = feature_set_playlist.sum()

    # filter feature_set to only include tracks not in the playlist
    feature_set_nonplaylist = feature_set[~feature_set['id'].isin(playlist_df)]

    return playlist_vector, feature_set_nonplaylist


def get_recommendations(playlist_df, num_recommendations=5):
    '''
    Generate music recommendations.
    '''
    playlist_vector, feature_set_nonplaylist = _get_playlist_vector(
        playlist_df)

    # filter tracks to only include tracks not in the playlist
    nonplaylist_tracks = tracks[tracks['id'].isin(
        feature_set_nonplaylist['id'].values)]

    # calculate cosine similarity between the playlist and each non-playlist track
    nonplaylist_tracks['similarity'] = cosine_similarity(feature_set_nonplaylist.drop(
        'id', axis=1).values, playlist_vector.values.reshape(1, -1))[:, 0]

    return nonplaylist_tracks.sort_values('similarity', ascending=False).head(num_recommendations)
