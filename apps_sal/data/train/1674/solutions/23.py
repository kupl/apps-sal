class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        dp = dict()

        def dfs(i, m):
            if m >= len(piles) - i:
                return sum(piles[i:])
            elif (i, m) in dp:
                return dp[i, m]
            else:
                dp[i, m] = max([sum(piles[i:]) - dfs(i + idx + 1, max(m, idx + 1)) for idx in range(2 * m)])
                return dp[i, m]
        return dfs(0, 1)
