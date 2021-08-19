class Solution:

    def longestAwesome(self, s: str) -> int:
        F = {0: -1}
        res = 0
        mask = 0
        for (j, c) in enumerate(s):
            mask ^= 1 << int(c)
            if mask not in list(F.keys()):
                F[mask] = j
            else:
                res = max(res, j - F[mask])
            for i in range(10):
                new_mask = mask ^ 1 << i
                if new_mask in list(F.keys()):
                    res = max(res, j - F[new_mask])
        return res
