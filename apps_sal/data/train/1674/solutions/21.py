class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @lru_cache(None)
        def dp(i, m):
            if i == n:
                return 0, 0
            s = 0
            a, b = 0, 10 ** 8
            for j in range(min(2 * m, n - i)):
                s += piles[i + j]
                c, d = dp(i + j + 1, max(j + 1, m))
                a = max(a, s + d)
                b = min(b, c)
            return a, b
        return dp(0, 1)[0]
