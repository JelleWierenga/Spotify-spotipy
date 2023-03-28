# Spotify Top Tracks

This is a Python script that connects to the Spotify API and retrieves the user's top tracks. The top tracks are displayed in the console.

## Prerequisites

- Python 3 installed on your computer
- A Spotify account
- A Spotify Developer account

## Installation

1. Clone the repository or download the script to your local machine.
2. Install the `spotipy` library by running `pip install spotipy` in the command line.

## Usage

1. Create a Spotify Developer account and register your application to get a client ID and client secret. Add `http://localhost:8888/callback` to the list of redirect URIs.
2. Replace the `client_id` and `client_secret` variables in the script with your own client ID and client secret.
3. Run the script in the command line using `python spotify_top_tracks.py`.

The script will ask you to authenticate with Spotify using the browser. Once authenticated, the script will retrieve your top tracks and display them in the console.

## Customization

You can customize the number of top tracks to retrieve by changing the `limit` parameter in the `current_user_top_tracks` function. You can also change the time range of the top tracks by changing the `time_range` parameter to `long_term`, `medium_term`, or `short_term`.

## License

This script is licensed under the MIT License. See `LICENSE` for more information.
