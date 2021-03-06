class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0 for m in range(n)] for i in range(n)]
        sufsum = [0] * (n + 1)
        for i in reversed(range(n)):
            sufsum[i] = sufsum[i + 1] + piles[i]
        return self.dfs(piles, 0, dp, sufsum, 1)

    def dfs(self, piles, index, dp, sufsum, M):
        if index == len(piles):
            return 0
        if dp[index][M] > 0:
            return dp[index][M]
        s = 0
        result = 0
        for i in range(index, index + 2 * M):
            if i >= len(piles):
                break
            s += piles[i]
            X = i - index + 1
            result = max(result, s + sufsum[i + 1] - self.dfs(piles, i + 1, dp, sufsum, max(X, M)))
        dp[index][M] = result
        return dp[index][M]
