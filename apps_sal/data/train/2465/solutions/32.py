class Solution:
    def divisorGame(self, N: int) -> bool:
        # dp solution
        d = {}

        def dp(v):
            if v not in d:
                d[v] = False
                for w in range(1, v):
                    if v % w == 0:
                        d[v] = d[v] or not dp(v - w)
            return d[v]
        out = dp(N)
        return out
