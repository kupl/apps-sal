class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        A, n = piles, len(piles)
        for i in range(n - 2, -1, -1):
            A[i] += A[i + 1]

        @lru_cache(maxsize=None)
        def helper(i, m):
            if i + 2 * m >= len(piles):
                return A[i]
            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, A[i] - helper(i + x, max(m, x)))
            return res

        return helper(0, 1)
