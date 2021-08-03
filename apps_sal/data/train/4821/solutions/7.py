class FileMaster():
    def __init__(self, filepath):
        self.path = filepath
        self._start_path = filepath.split('/')[:-1]
        self._end_path = filepath.split('/')[-1].split('.')

    def extension(self):
        return self._end_path[1]

    def filename(self):
        return self._end_path[0]

    def dirpath(self):
        return '/'.join(self._start_path) + '/'
