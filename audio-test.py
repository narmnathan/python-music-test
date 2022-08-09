import pygame, tinytag
from pygame import mixer
# reading from user songs, allow user to play, pause, and skip to next/previous song
# may implement reading from queue before from user songs

class Player:
    def __init__(self):
        pygame.init()
        mixer.init()
        self.songs = {'Don t Worry Feat Cash Out': '/Users/narmnathan/Music/pndcolours/04 - Don t Worry Feat Cash Out.mp3',
                      'Juss Know Feat Travis Scott': '/Users/narmnathan/Music/pndcolours/03 - Juss Know Feat Travis Scott.mp3',
                      'Girl From Oakland': '/Users/narmnathan/Music/pndcolours/02 - Girl From Oakland.mp3',
                      'Let s Get Married': '/Users/narmnathan/Music/pndcolours/01 - Let s Get Married.mp3'}
        # currently a placeholder

    def play(self):
        for key in self.songs:
            print('%s' % (key))
        user_choice = input('enter the name of a song to play: \n')
        if user_choice in self.songs:
            path = self.songs[user_choice]
            mixer.music.load(path)
            mixer.music.play()
        else:
            print('invalid input.')
            self.play()
        if mixer.music.get_busy() is True:
            path = self.songs[user_choice]
            tag = tinytag.TinyTag.get(path)
            title = tag.title
            artist = tag.artist
            album = tag.album
            # likely will change w/ introduction of queue module and distinct storing system
            print('now playing: %s by %s' % (title, artist))

    def pause(self):
        if mixer.music.get_busy() is True:
            mixer.music.pause()




player = Player()
player.play()