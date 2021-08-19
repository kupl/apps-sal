class Solution:

    def longestAwesome(self, s: str) -> int:
        seen = [len(s)] * (1 << 10)
        seen[0] = -1
        mask = 0
        res = 0
        for (i, char) in enumerate(s):
            mask ^= 1 << int(char)
            res = max(res, i - seen[mask])
            for j in range(10):
                temp = 1 << j ^ mask
                res = max(res, i - seen[temp])
            seen[mask] = min(seen[mask], i)
        return res
