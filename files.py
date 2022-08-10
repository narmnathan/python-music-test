import os, glob, tinytag
# establish directory to read and import music files from
# allow user to set directory and choose files to import
# imported files are stored and returned in user's Songs list


class fileSystem:
    def __init__(self):
        self.dir = os.path.expanduser('~/Music')
        self.songs = {}

    def listdir(self):
        # prints mp3 files in current directory
        # update to include .wav
        directory = glob.glob(self.dir + '/*.mp3')
        os.listdir(self.dir)
        if not directory:
            print('no mp3 files found! \n')
        else:
            print(directory)
        user_choice = input('[1] to set directory, [2] to import files, [3] to exit \n')
        if user_choice == '1':
            os.system('clear')
            self.chdir()
        elif user_choice == '2':
            if not directory:
                print('no mp3 files to import... \n')
                os.system('clear')
                self.listdir()
            else:
                os.system('clear')
                self.file_import()
        else:
            print('exiting...')

    def chdir(self):
        # prints directory and allows user to set path
        print('current directory: ' + self.dir)
        print(os.listdir(self.dir))
        user_choice = input('enter directory to read: ')
        # change later
        while True:
            if os.path.isdir(user_choice) is True:
                os.system('clear')
                self.dir = user_choice
                os.chdir(self.dir)
                self.listdir()
                break
            elif os.path.isdir('%s/%s' % (self.dir, user_choice)) is True:
                os.system('clear')
                self.dir = '%s/%s' % (self.dir, user_choice)
                os.chdir(self.dir)
                self.listdir()
                break
            else:
                os.system('clear')
                print('invalid input. \n')
                self.chdir()
                break

    def file_import(self):
        i = 1
        for index in glob.glob(self.dir + '/*.mp3'):
            tag = tinytag.TinyTag.get(index)
            print('[%s] - %s' % (i, tag.title))
            i += 1
        user_choice = input('enter [0] to import all listed files: \n')
        # update to have user choose range of songs to import
        if user_choice == '0':
            for index in glob.glob(self.dir + '/*.mp3'):
                tag = tinytag.TinyTag.get(index)
                self.songs[tag.title] = index
                os.system('clear')
                print('success!')
        # ideally this will import all files to user's Songs list


file = fileSystem()
file.listdir()
