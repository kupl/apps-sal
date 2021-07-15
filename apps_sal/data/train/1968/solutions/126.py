class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        s = sorted(folder)
        fs = []
        while s:
            fs.append(s[0])
            s.pop(0)
            while s and self.is_subfolder(fs[-1], s[0]):
                s.pop(0)
        return fs
    def is_subfolder(self, x,y):
        x = x.split('/')
        y = y.split('/')
        if len(x) >= len(y):
            return False
        for i, c in enumerate(x):
            if c != y[i]:
                return False
        return True
