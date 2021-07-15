from collections import Counter

class Solution:
    def longestAwesome(self, s: str) -> int:
        seen = {0: -1}
        res, prefix = 0, 0
        
        for i, num in enumerate(map(int, s)):
            prefix ^= 1 << num
            res = max(res, i - seen.get(prefix, float('inf')))
            for k in range(10):
                prefix_add_odd = prefix ^ (1 << k)
                res = max(res, i - seen.get(prefix_add_odd, float('inf')))
            seen.setdefault(prefix, i)
        
        return res

