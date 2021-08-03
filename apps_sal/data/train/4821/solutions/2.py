class FileMaster():
    def __init__(self, filepath):

        i = len(filepath) - 1
        while filepath[i] != ".":
            i -= 1
        indexExt = i

        while filepath[i] != "/":
            i -= 1

        self.ext = filepath[indexExt + 1:]
        self.filen = filepath[i + 1:indexExt]
        self.dirp = filepath[:i + 1]

    def extension(self): return self.ext

    def filename(self): return self.filen

    def dirpath(self): return self.dirp
