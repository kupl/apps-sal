class FileMaster():
    def __init__(self, filepath):
        self.path=filepath
        self.dot=self.path.index(".")
        self.slash=self.path[::-1].index("/")
    def extension(self):
        return self.path[self.dot+1:]
    def filename(self):
        return self.path[-self.slash:self.dot]
    def dirpath(self):
        return self.path[:-self.slash]
