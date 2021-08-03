class Solution:
    def longestAwesome(self, s: str) -> int:
        cur = res = 0
        check = defaultdict(lambda: float('inf'))
        check[0] = -1
        for i, c in enumerate(s):
            c = int(c)
            cur ^= 1 << c
            res = max(res, i - check[cur])
            for a in range(10):
                res = max(res, i - check[cur ^ (1 << a)])
            check[cur] = min(check[cur], i)
        return res
