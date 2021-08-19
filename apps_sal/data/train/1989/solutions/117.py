class Solution:

    def longestAwesome(self, s: str) -> int:
        n = len(s)
        res = 0
        mask = 0
        idx = [n + 1] * 1024
        idx[0] = -1
        for (i, c) in enumerate(s):
            mask ^= 1 << ord(c) - ord('0')
            res = max(res, i - idx[mask])
            for j in range(10):
                res = max(res, i - idx[mask ^ 1 << j])
            idx[mask] = min(idx[mask], i)
        return res
