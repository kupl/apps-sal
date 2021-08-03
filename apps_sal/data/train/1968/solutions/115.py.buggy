class Directory:
    
    def __init__(self, name=\"\"):
        self.name = name
        self.subDirectories = {}
        self.flg=False

class Solution:
    
    def __init__(self):
        self.root = Directory()
        
    def generate(self, directory):
        if directory.flg:
            return [[directory.name]]
        res = []
        for k in directory.subDirectories.keys():
            res += self.generate(directory.subDirectories[k])
        for r in res:
            r.append(directory.name)
        return res
        
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        for f in folder:
            directories = re.split('/', f)[1:]
            cur = self.root
            for i, d in enumerate(directories):
                if cur.flg:
                    break
                if d not in cur.subDirectories.keys():
                    cur.subDirectories[d] = Directory(d)
                cur = cur.subDirectories[d]
                if i == len(directories) - 1:
                    cur.flg = True
        
        ans = self.generate(self.root)
        return ['/'.join(a[::-1]) for a in ans]
        
