# Spotify: BPM Playlist Creator
A simple python3 script using spotipy library to search for an artist, then create a playlist of all of their songs in order of increasing bpm

Super duper simple script, it's probably not structured very well, the search function is somewhat unfinished, etc.

But hey, it works.

# Install

## 1) With pipenv
I recommend using pipenv to manage dependencies. I'm not yet a python expert, so I'll let you do your own [research](https://pythontips.com/2013/07/30/what-is-virtualenv/).

Basically, install pipenv:
```bash
brew install pipenv
```

Use it to create the environment and install dependencies:
```bash
git clone https://github.com/jkimminau/spotify_bpm_playlist_creator my_clone
cd my_clone
pipenv install
```

Run a shell in the virutualenv:
```bash
pipenv shell
```

## 2) Install spotipy on your machine
```bash
git clone https://github.com/jkimminau/spotify_bpm_playlist_creator my_clone
cd my_clone
sudo pip3 install spotipy
```

# Running

You need your own Spotify API keys, you can get them [here](https://developer.spotify.com/dashboard/).
Then, replace the strings in the following lines and run them:
```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='https://example.com/callback'
```
Note that these say *SPOTIPY*, and not *SPOTIFY*.
There's also nothing to replace in the third line, just run it.

Lastly, to run the script, just use:
```bash
python3 bpm_script.py
```

Then, it'll run. If you've not authenticated it before, you made need to post the link you are redirected to after you click 'Allow' on the webpage it opens. Even if it says `This page is unavailable`, still paste that link in the console, that's not a error.

If you have any questions/suggestions, go ahead and email me at thepistochini@gmail.com. Thanks!
