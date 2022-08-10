import os, tinytag
# will take any imported files and sort/identify based on metadata
# creates initial list of user's songs
# any item in initial list pairs to dict with item's metadata values


class userStorage:
    def __init__(self):
        self.files = '/Users/narmnathan/Music/pndcolours'
        self.songs = {'Don t Worry Feat Cash Out': '/Users/narmnathan/Music/pndcolours/04 - Don t Worry Feat Cash Out.mp3',
                      'Juss Know Feat Travis Scott': '/Users/narmnathan/Music/pndcolours/03 - Juss Know Feat Travis Scott.mp3',
                      'Girl From Oakland': '/Users/narmnathan/Music/pndcolours/02 - Girl From Oakland.mp3',
                      'Let s Get Married': '/Users/narmnathan/Music/pndcolours/01 - Let s Get Married.mp3'}
        self.list = {}

        # placeholder
    def dict(self):
        for key in self.songs:
            tag = tinytag.TinyTag.get(self.songs[key], image=True)
            title = tag.title
            artist = tag.artist
            album = tag.album
            duration_min = int(((tag.duration) / 60))
            duration = (str(duration_min) + ':' + str((int(tag.duration - (duration_min * 60)))))
            cover = tag.get_image()
            self.list[title] = dict(title = tag.title,
                                    artist = artist,
                                    album = album,
                                    duration = duration,
                                    cover = cover)

    # def update(self):





user = userStorage()
user.dict()
