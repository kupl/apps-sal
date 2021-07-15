class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = {}
        for f in folder:
            f = f.split(\"/\")[1:]
            self.insert(root, f)
        return self.dfs([], root, [])
        
    def insert(self, root, f):
        for e in f:
            if e not in root:
                root[e] = {}
            root = root[e]
        root['#'] = '#'
    
    def dfs(self, tmp, root, fn):
        if '#' in root:
            fn.append('/' + '/'.join(tmp))
            return fn
        for k in root:
            #if k != '#':
            self.dfs(tmp+[k], root[k], fn)
        return fn
            
        
