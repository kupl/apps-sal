class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for x in folder:
            cur = x.split('/')
            if not res or res[-1] != cur[:len(res[-1])]:
                res.append(cur)
        
        return [ \"/\".join(x) for x in res ]
            
        
