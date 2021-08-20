class FileMaster:

    def __init__(self, filepath):
        lk = filepath.rfind('.')
        ls = filepath.rfind('/')
        self.ext = filepath[lk + 1:]
        self.file = filepath[ls + 1:lk]
        self.path = filepath[:ls + 1]

    def extension(self):
        return self.ext

    def filename(self):
        return self.file

    def dirpath(self):
        return self.path
