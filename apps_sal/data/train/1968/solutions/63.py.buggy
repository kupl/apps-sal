class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        folder.sort(key = lambda x: len(x))
        res = []
        # while folder:
        #     e = folder.pop()
        #     for p in folder:
        #         if e.startswith(p) and e[len(p)] == '/':
        #                 e = ''   
        #                 break
        #     if e: res.append(e)
        # return res
    
        trie = defaultdict(dict)
        for t in folder:
            m = trie
            parent = False
            for c in t.split('/'):
                
                if c in m: m = m[c]
                else: 
                    m[c] = {}
                    m = m[c]
                if '$' in m: 
                    parent = True
                    break
            if not parent:
                m[\"$\"] = '$'
                res.append(t)
        return res
            
