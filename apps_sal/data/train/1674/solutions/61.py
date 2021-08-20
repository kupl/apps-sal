class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        l = len(piles)
        dp = [[[-1 for i in range(l)] for j in range(2 * l)] for k in range(2)]

        def game(piles, M, pos, player):
            total = 0
            if pos >= l:
                return 0
            if dp[player][pos][M] != -1:
                return dp[player][pos][M]
            if player == 0:
                maxsum = 0
                for X in range(1, 2 * M + 1):
                    maxsum = max(maxsum, sum(piles[pos:pos + X]) + game(piles, max(M, X), pos + X, not player))
                dp[player][pos][M] = maxsum
                return maxsum
            else:
                minsum = sys.maxsize
                for X in range(1, 2 * M + 1):
                    minsum = min(minsum, game(piles, max(M, X), pos + X, not player))
                dp[player][pos][M] = minsum
                if minsum == sys.maxsize:
                    return 0
                return minsum
        return game(piles, 1, 0, 0)
