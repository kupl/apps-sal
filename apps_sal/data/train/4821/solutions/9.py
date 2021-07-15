class FileMaster():
    def __init__(self, filepath):
        self.arr = filepath.split('/')
    def extension(self):
        return self.arr[-1].split('.')[1]
    def filename(self):
        return self.arr[-1].split('.')[0]
    def dirpath(self):
        self.arr[-1] = ''
        return '/'.join(self.arr)
