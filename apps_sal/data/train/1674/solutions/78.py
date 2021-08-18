
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        if len(piles) <= 2:
            return sum(piles)
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]
        piles.append(0)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for pile in reversed(range(n)):
            for M in reversed(range(n)):
                nextPlayerMaximum = piles[pile]
                for nextPile in range(pile + 1, min(pile + 2 * M + 1, n + 1)):
                    nextPlayerMaximum = min(nextPlayerMaximum, dp[nextPile][max(M, nextPile - pile)])
                dp[pile][M] = piles[pile] - nextPlayerMaximum

        return dp[0][1]
