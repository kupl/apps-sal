class Solution:
    def longestAwesome(self, s: str) -> int:
        d = defaultdict(lambda: 1e20)
        d[0] = -1
        res = 0
        mask = 0
        for i, val in enumerate(s):
            mask ^= 1 << int(val)
            d[mask] = min(d[mask], i)
            res = max(res, i - d[mask])
            for k in range(11):
                res = max(res, i - d[mask ^ (1 << k)])
        return res
