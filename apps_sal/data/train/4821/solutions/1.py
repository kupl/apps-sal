class FileMaster:

    def __init__(self, filepath):
        self.fp = filepath

    def extension(self):
        return self.fp.split('.')[-1]

    def filename(self):
        return self.fp.rsplit('/', 1)[-1].split('.')[0]

    def dirpath(self):
        return self.fp.rsplit('/', 1)[0] + '/'
