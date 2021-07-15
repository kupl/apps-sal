class Solution:
    def longestAwesome(self, s: str) -> int:
        rec = 0
        seen = {0:-1}
        mask = 0
        
        for i,n in enumerate(s):
            mask ^= (1<<int(n))
            if mask in seen:
                rec = max(rec, i - seen[mask])
            else:
                seen[mask] = i
            for d in range(10):
                omask = mask ^ (1<<d)
                if omask in seen:
                    rec = max(rec, i - seen[omask])
        
        return rec
