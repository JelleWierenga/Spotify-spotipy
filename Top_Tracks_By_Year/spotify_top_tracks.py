import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id="your_client_id", client_secret="your_client_secret", redirect_uri="http://localhost:8888/callback"))

year = input("What year do you want to know: ")

results = sp.search(f"year:{year}", type="track", limit=50)

track_ids = [track['id'] for track in results['tracks']['items']]

playlist_name = f"Top Tracks of {year}"
playlist_description = f"A playlist of the top tracks released in {year}"

playlist = sp.user_playlist_create(sp.current_user()['id'], playlist_name, public=True, description=playlist_description)

sp.playlist_add_items(playlist['id'], track_ids)

print(f"Top Tracks of {year}:")
for idx, track in enumerate(results['tracks']['items']):
    print(f"{idx+1} - {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
