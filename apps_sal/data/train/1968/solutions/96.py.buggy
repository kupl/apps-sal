class Trie():
    def __init__(self):
        self.children = {}
        
    def put(self, s):
        s = s.split(\"/\")
        check = self.children
        for c in s[1:]:
            if c not in check:
                check[c] = {}
            check = check[c]
        check[-1] = True
    
    def find(self, s):
        s = s.split(\"/\")
        check = self.children
        for c in s[1:]:
            if c not in check:
                return False
            check = check[c]
        return -1 in check
            
    

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ret = []
        def dfs(children, build):
            if -1 in children:
                ret.append(\"/\"+\"/\".join(build))
                return
            for c in children:
                dfs(children[c], build+[c])
                
        trie = Trie()
        
        for f in folder:
            #print(f)
            trie.put(f)
        #print(trie.children)
        check = trie.children
        stack = []
        dfs(check, [])
        return ret
                
        \"\"\"
        d = {}
        ret = []
        folder.sort()
        for f in folder:
            fl = f.split(\"/\")
            for i in range(1, len(fl)):
                tup_h = tuple(fl[1:i+1])
                if tup_h in d:
                    break
                elif i == len(fl)-1:
                    d[tup_h] = f
                    ret.append(f)
        return ret
        \"\"\"
