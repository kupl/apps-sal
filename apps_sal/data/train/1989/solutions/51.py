class Solution:
    def longestAwesome(self, s: str) -> int:
        
        
        targets = {1 << x for x in range(10)}
        targets.add(0)
        
        print(targets)
        seen = {}
        res = 0
        prev = 0
        seen[0] = -1
        for idx, char in enumerate(s):
            curr = prev ^ 1<<int(char)
            if curr not in seen:
                seen[curr] = idx
                
            for target in targets:
                if curr ^ target in seen:
                    res = max(res, idx - seen[curr ^ target])
                    
            prev = curr
        print(seen)
        print(res)
        return res
                    

