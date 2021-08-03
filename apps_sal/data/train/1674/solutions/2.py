class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        for i in range(len(piles) - 2, -1, -1):
            piles[i] += piles[i + 1]

        memo = {}

        def dfs(i, m):
            if i + (2 * m) >= len(piles):
                return piles[i]
            if (i, m) in memo:
                return memo[(i, m)]

            memo[(i, m)] = piles[i] - min((dfs(i + j, max(m, j))) for j in range(1, (2 * m) + 1))
            return memo[(i, m)]

        return dfs(0, 1)
