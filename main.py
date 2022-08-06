# to-do: needs to be able to read files, read metadata from files, organize albums/tracks, and play songs
# to-do: add a way for user to specify filepath of folder before execution

from tinytag import TinyTag
from pathlib import Path
from playsound import playsound

filepath = '/Users/narmnathan/Documents/Music/PNDCOLOURS/02 - Girl From Oakland.mp3'

tag = TinyTag.get(filepath)

album = tag.album
artist = tag.artist
title = tag.title

def play():
    print(('Now Playing: %s -- %s, %s') % (title, artist, album))
    playsound(filepath)

while True:
    print('enter \'play\' to play, \'pause\' to pause, or \'skip\' to skip:')
    choice = input()
    if choice == 'play':
        play()
