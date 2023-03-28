# Spotify Top Tracks Playlist Generator

This is a simple Python script that generates a Spotify playlist of the top tracks released in a given year.

## Setup

1. Clone this repository or download the `spotify_top_tracks.py` file.
2. Install the required packages using pip: `pip install spotipy`

3. Create a Spotify developer account and a new app to obtain a client ID and client secret.
4. In the Spotify developer dashboard, add `http://localhost:8888/callback` as a redirect URI for your app.
5. Replace the placeholders in the script with your own Spotify client ID and client secret.

## Usage

1. Run the script:`python spotify_top_tracks.py`

2. Enter the year for which you want to generate the playlist.
3. The script will search for the top 50 tracks released in the given year and create a new public playlist with the name `Top Tracks of [year]` and a description `A playlist of the top tracks released in [year]`.
4. The script will then add the top tracks to the newly created playlist.
5. The script will print a list of the top tracks with their names and artists.

Note: You must have a Spotify Premium account to modify and create public playlists.

## License

This project is licensed under the terms of the MIT license. You can find a copy of the license in the `LICENSE` file.
