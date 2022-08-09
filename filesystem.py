import os, glob, tinytag, playsound
# to-do: introduce play/pause/skip functionality, save user_playlist to file ?
# to-do: sort out pygame mp3 functionality
# file now obsolete -- refer to file-test

class fileSystem:
    default_path = os.path.expanduser('~/Music')
    default_listdir = os.listdir(default_path)

    def __init__(self):
        self.path = os.path.expanduser('~/Music') # default user Music path
        self.playlist = {} # import music to here

    def import_file(self, default_listdir=os.listdir(default_path)): # import folders to sort into dictionary as per import_dict():
        print(default_listdir)  # show all folders in Music directory
        while True:
            file_input = input('enter the name of the folder or file to import: \n')
            file_path = '%s/%s' % (self.path, file_input)
            if os.path.isdir(file_path):
                os.chdir(file_path)
                self.path = os.getcwd()
                print(self.path)
                print(os.listdir(self.path))
                user_choice = input('enter \'import\' to import: \n')
                if user_choice == 'import':
                    fileSystem.import_dict(self)
                break
            else:
                print(file_path + ' does not exist.')
                continue

    def import_dict(self): # have Python take the file names in a folder, sort them, and assign them keys that are path
        file_path = self.path
        print(file_path)
        glob_list = file_path + '/*.mp3'
        print(glob_list)
        import_list = glob.glob(glob_list)
        import_list.sort()
        print(import_list)
        for index in import_list:
            print(index)
            tag = tinytag.TinyTag.get(index)
            self.playlist[tag.title] = index
        user_choice = input('enter \'playlist\' to see playlist: \n')
        if user_choice == 'playlist':
            self.user_playlist()

    def user_playlist(self): # display user playlist
        for number, key in enumerate(self.playlist, start=1):
            print(str(number) + ' - ' + str(key))
        self.play_song()

    def play_song(self): # play songs from playlist
        user_select = input('enter the name of a song to play: \n')
        while True:
            tag = tinytag.TinyTag.get(self.playlist[str(user_select)])
            album = tag.album
            artist = tag.artist
            title = tag.title

            print('now playing: %s - %s, %s' % (title, artist, album))
            playsound.playsound(self.playlist[str(user_select)])


filesystem = fileSystem()
filesystem.import_file()