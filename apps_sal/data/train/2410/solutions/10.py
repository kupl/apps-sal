class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        t = self.count(name)
        s = self.count(typed)
        if len(t) != len(s):
            return False
        
        for tt, ss in zip(t, s):
            if tt[0] != ss[0]:
                return False
            
            if tt[1] > ss[1]:
                return False
            
        return True
        
        
    def count(self, s):
        res = []
        prev = None
        cnt = 0
        for c in s:
            if c == prev:
                cnt += 1
            elif cnt > 0:
                res.append((c, cnt))
                cnt = 1
            else:
                cnt = 1
                
            prev = c
            
        return res

