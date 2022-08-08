import pygame, ffmpeg
from pygame import mixer

class Player:
    pygame.init()
    mixer.init()

    def __init__(self):
        self.player = mixer.music
        self.queue = []

    def user_queue(self):
        for index in self.queue:
            print(index)
            self.player.load(index)


    def play(self): # play songs
        self.queue.append('/Users/narmnathan/Music/PNDCOLOURS/02 - Girl From Oakland.mp3')
        self.user_queue()
        # figure out how to connect import functionality into player functionality
        self.player.play()
        if self.player.play() is None:
            print("now playing...")

    def pause(self):
        self.player.pause()


mixer.init()
Player = Player()
Player.play()
