import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from yt_dlp import YoutubeDL
from urllib.parse import urlparse, parse_qs

def remove_query_params(url):
    parsed_url = urlparse(url)
    clean_url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
    return clean_url

def get_playlist_tracks(playlist_url):
    clean_playlist_url = remove_query_params(playlist_url)
    client_id = 'put your client id here'
    client_secret = 'put your client secret here'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    playlist_id = clean_playlist_url.split('/')[-1]
    results = sp.playlist_tracks(playlist_id)
    track_titles = []

    track_titles.extend([track['track']['name'] for track in results['items']])
    while results['next']:
        results = sp.next(results)
        track_titles.extend([track['track']['name'] for track in results['items']])
    return track_titles

def search_and_download(query):
    output_folder = 'outputs'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(['ytsearch:' + query])

if __name__ == "__main__":
    playlist_url = input("Enter Spotify playlist URL: ")
    tracks = get_playlist_tracks(playlist_url)
    if tracks:
        for track in tracks:
            print("Searching for:", track)
            search_and_download(track)
            print("Downloaded:", track)
