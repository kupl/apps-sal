class FileMaster():
    def __init__(self, f): self.path, self.ex = f.rsplit('/', 1)
    def extension(self): return self.ex.split('.')[1]
    def filename(self): return self.ex.split('.')[0]
    def dirpath(self): return self.path + '/'
