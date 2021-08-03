class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath

    def extension(self):
        return self.filepath.rsplit('.', 1)[-1]

    def filename(self):
        return self.filepath.rsplit('/', 1)[-1].rsplit('.', 1)[0]

    def dirpath(self):
        return self.filepath[:self.filepath.rfind('/') + 1]
