class Solution:
    def longestAwesome(self, s: str) -> int:
        res, cur, n = 0, 0, len(s)
        seen = [-1] + [n] * 1024
        for i, c in enumerate(s):
            cur ^= 1 << int(c)
            for a in range(10):
                res = max(res, i - seen[cur ^ (1 << a)])
            res = max(res, i - seen[cur])
            seen[cur] = min(seen[cur], i)
        return res
