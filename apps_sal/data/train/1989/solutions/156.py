class Solution:

    def longestAwesome(self, s: str) -> int:
        cur = res = 0
        d = defaultdict(lambda: float('inf'))
        d[0] = -1
        for (i, ch) in enumerate(s):
            cur ^= 1 << int(ch)
            res = max(res, i - d[cur])
            for j in range(10):
                res = max(res, i - d[cur ^ 1 << j])
            d[cur] = min(d[cur], i)
        return res
