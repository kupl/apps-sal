class FileMaster:

    def __init__(self, filepath):
        self.path = filepath

    def extension(self):
        return self.path[self.path.index('.') + 1:]

    def filename(self):
        return self.path[-self.path[::-1].index('/'):self.path.index('.')]

    def dirpath(self):
        return self.path[:-self.path[::-1].index('/')]
