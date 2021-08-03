class FileMaster():
    def __init__(self, filepath):
        self.f_file = filepath.split('/')
        self.f_name, self.extn = self.f_file[-1].split('.')

    def extension(self):
        return self.extn

    def filename(self):
        return self.f_name

    def dirpath(self):
        return '/'.join(self.f_file[:-1]) + '/'
