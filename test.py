import os, glob
path = os.path.expanduser('~/Music')
listdir = os.listdir(path)
print(listdir) # show all folders in Music directory
#playlist = {}

class UserImport:
    def __init__(self, path):
        self.path = os.path.expanduser('~/Music')

    def import_file(self): # import folders to sort into dictionary as per import_dict():
        while True:
            file_input = input('enter the name of the folder or file to import:')
            file_path = '%s/%s' % (path, file_input)
            if os.path.isdir(file_path):
                os.chdir(file_path) # change this to import folder/file into a dictionary that stores the song name as key and path as value
                self.path = os.getcwd()
                print(self.path)
                print(os.listdir(self.path))
                user_choice = input('enter \'import\' to import:')
                if user_choice == 'import':
                    UserImport.import_dict(self)
                break
            else:
                print(file_path + ' does not exist.')
                continue

    def import_dict(self): # have Python take the file names in a folder, sort them, and assign them keys that are path
        file_path = self.path
        # print('now importing...')
        print(file_path)
        #print(os.listdir(file_path))
        import_playlist = list(os.listdir(file_path))
        sorted(import_playlist, reverse=True)
        print(import_playlist)







user_import = UserImport(path)
user_import.import_file()