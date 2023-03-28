import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id="your client_id", client_secret="your client_secret", redirect_uri="http://localhost:8888/callback"))

results = sp.current_user_top_tracks(time_range='short_term', limit=5)

for idx, track in enumerate(results['items']):
    print(f"{idx+1} - {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
