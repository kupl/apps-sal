class Solution:
    def longestAwesome(self, s: str) -> int:
        bitmask = {}
        mask = 0
        ans = 1
        n = len(s)
        bitmask[0] = -1
        for i in range(n):
            mask ^= (1 << int(s[i]))
            if(mask in bitmask):
                ans = max(ans, i - bitmask[mask])
            for j in range(10):
                test = mask ^ (1 << j)
                if(test in bitmask):
                    ans = max(ans, i - bitmask[test])
            if(mask not in bitmask):
                bitmask[mask] = i
        return ans
