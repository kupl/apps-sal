class Solution:
    def longestAwesome(self, s: str) -> int:
        d = {}
        d[0] = -1
        sm, res = 0, 0
        for i, c in enumerate(s):
            sm ^= 1 << int(c)
            if sm in d:
                res = max(res, i - d[sm])
            else:
                d[sm] = i
            for j in range(10):
                msk = sm ^ (1 << j)
                if msk in d and i - d[msk] > res:
                    res = i - d[msk]
        return res
