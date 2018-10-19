# spotify_bpm_playlist_creator
A simple python script using spotipy library to search for an artist, then create a playlist of all of their songs in order of increasing bpm

Super duper simple script, it's probably not structured very well, the search function is somewhat unfinished, etc.

But hey, it works.

#Install

I recommend using pipenv to manage dependencies. I'm not yet a python expert, so I'll let you do your own [research](https://pythontips.com/2013/07/30/what-is-virtualenv/).

Basically, install pipenv:
```
brew install pipenv
```

Use it to create the environment and install dependencies:
```
git clone https://github.com/jkimminau/spotify_bpm_playlist_creator my_clone
cd my_clone
pipenv install
```

Run a shell in the virutualenv:
```
pipenv shell
```

You need your own Spotify API keys, you can get them [here](https://developer.spotify.com/dashboard/).
Then, replace the strings in the following lines and run them:
```
