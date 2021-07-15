class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        marks, t = 0, list(target)
        res = []
        visited = set()
        while marks < len(target):
            found = False
            for i in range(len(t) - len(stamp) + 1):
                if i not in visited and self.canReplace(stamp, t,i):  
                    marks += self.replace(stamp,t,i)
                    res.append(i)  
                    visited.add(i)  
                    found = True
                if marks >= len(target): break
            if not found: return []

        return res[::-1]
    
    def canReplace(self, s,t, j): 
        for i in range(len(s)):    
            if t[j+i] != \"*\" and s[i] != t[j+i]:                
                return False               
        return True
    
    def replace(self, s,t, j):
        count = 0
        for i in range(len(s)):
            if t[i+j] != \"*\":
                t[i+j] = \"*\"
                count += 1
        return count
        
