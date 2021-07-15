class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        trie[\"/\"] = False   # whether it's a folder
        
        for f in folder:
            paths = f.split(\"/\")
            current = trie
            n = len(paths)
            for i in range(1,n):
                p = paths[i]
                if p not in current:
                    current[p] = {}
                current = current[p]
                if i==n-1:  current[\"/\"] = True
                else:
                    if \"/\" not in current:  current[\"/\"] = False
                
                
        print(trie)
        
        self.ans = []
        def findPath(path, result):
            if path[\"/\"]:
                self.ans.append(result)
                return
            for k, v in path.items():
                if k == \"/\":    continue
                findPath(v, result+[k])
            
        result = []
        findPath(trie, result)
        return [\"/\" + \"/\".join(a) for a in self.ans]
            
