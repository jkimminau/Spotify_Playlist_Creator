import spotipy
import spotipy.util as util
import json
from spotipy.oauth2 import SpotifyClientCredentials

#print(json.dumps(results, sort_keys=True, indent=4, separators=(',', ': ')))

#client_credentials_manager = SpotifyClientCredentials()
#sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def list_artists(artists):
	for i, t in enumerate(artists):
	    print (' ', i, t['name'])

def get_track_infos(artist_id):
	track_list = []
	albums = sp.artist_albums(artist_id=artist_id)
	for i, t in enumerate(albums['items']):
		if(t['album_type'] == 'album'):
			tracks = sp.album_tracks(album_id=t['uri'])
			for track in tracks['items']:
				j = {}
				j['uri'] = track['uri']
				j['name'] = track['name']
				track_list.append(j)
	return (track_list)

def add_features(track_list):
	tempo_list = []
	tmp_list = []
	for t in track_list:
		tmp_list.append(t['uri'])
		if (len(tmp_list) >= 50):
			features = sp.audio_features(tracks=tmp_list)
			for feature in features:
				tempo_list.append(feature['tempo'])
			tmp_list = []
	if (len(tmp_list) != 0):	
		features = sp.audio_features(tracks=tmp_list)
		for feature in features:
			tempo_list.append(feature['tempo'])

	for i, t in enumerate(track_list):
		t['tempo'] = tempo_list[i]
	return (track_list)

def add_tracks(user_id, playlist_id, track_list):
	tmp_list = []
	for uri in track_list:
		tmp_list.append(uri)
		if (len(tmp_list) >= 100):
			sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=tmp_list)
			tmp_list = []
	if (len(tmp_list) != 0):	
		sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=tmp_list)
		

user_id ='1225066737'
scope = 'playlist-modify-private playlist-modify-public playlist-read-collaborative playlist-read-private' 
token = util.prompt_for_user_token(user_id, scope, redirect_uri='https://localhost')
sp = spotipy.Spotify(auth=token)
sp.trace = False

artist = input("Enter an artists name: ")
results = sp.search(q=artist, limit=20, type='artist')
list_artists(results['artists']['items'])

selection = int(input("Select band (1 - 20): "))
if (selection == "x"):
	exit()

track_list = get_track_infos(results['artists']['items'][selection]['id'])
track_list = add_features(track_list)
track_list = sorted(track_list, key=lambda k: k['tempo'])
sorted_list = []
for track in track_list:
	print(track['name'] + " : " + str(track['tempo']))
	sorted_list.append(track['uri'])

confirm = input("Are you sure you'd like to create this playlist? (y/n):")
if (confirm != 'y' and confirm != 'Y'):
	exit()
playlist = sp.user_playlist_create(user=user_id, name=(results['artists']['items'][selection]['name'] + " - sorted by increasing BPM"), public=True)
add_tracks(user_id=user_id, playlist_id=playlist['id'], track_list=sorted_list)
