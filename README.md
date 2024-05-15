# Spotify-Downloader
This Python script allows you to download the audio of tracks from a Spotify playlist by searching for them on YouTube and downloading the audio.

## Requirements

Before running the script, you'll need to have the following:

- Python 3.10+ installed on your system.
- The `spotipy` library for accessing the Spotify Web API. You can install it via pip:
  ```
  pip install spotipy
  ```
- The `yt_dlp` library for downloading audio from YouTube. You can install it via pip:
  ```
  pip install yt-dlp
  ```

## How to Run

1. Clone or download this repository to your local machine.

2. Navigate to the directory containing the script.

3. Replace `'put your client id here'` and `'put your client secret here'` in the script with your Spotify API client ID and client secret. You can obtain these by creating an app in the Spotify Developer Dashboard: [https://developer.spotify.com/dashboard/applications](https://developer.spotify.com/dashboard/applications)

4. Run the script by executing the following command in your terminal:
   ```
   python main.py
   ```

5. Enter the Spotify playlist URL when prompted.

6. The script will search for each track in the playlist on YouTube and download its audio. The downloaded files will be saved in the `outputs` folder.

