import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-public user-top-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id="Client_id", client_secret="Client_secret   ", redirect_uri="http://localhost:8888/callback"))

playlist_name = "My Top 10 Tracks"
playlist_description = "A playlist of my top 10 most listened tracks"

playlist = sp.user_playlist_create(sp.current_user()['id'], playlist_name, public=True, description=playlist_description)

results = sp.current_user_top_tracks(time_range='short_term', limit=10)
track_ids = [track['id'] for track in results['items']]

sp.playlist_add_items(playlist['id'], track_ids)

print("Tracks added to playlist:")
for idx, track in enumerate(results['items']):
    print(f"{idx+1} - {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
