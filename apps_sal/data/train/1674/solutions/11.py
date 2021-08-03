class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        prefix = [0] * (len(piles) + 1)
        for i in range(len(piles)):
            prefix[i + 1] += prefix[i] + piles[i]
        return self.dfs(piles, memo, 0, 1, prefix)

    def dfs(self, piles, memo, i, m, prefix):
        if i == len(piles):
            return 0

        if (i, m) in memo:
            return memo[(i, m)]

        ans = float('-inf')
        for j in range(1, m + 1):
            if i + j <= len(piles):
                ans = max(ans, prefix[-1] - prefix[i] - self.dfs(piles, memo, i + j, m, prefix))

        for j in range(m + 1, 2 * m + 1):
            if i + j <= len(piles):
                ans = max(ans, prefix[-1] - prefix[i] - self.dfs(piles, memo, i + j, j, prefix))

        memo[(i, m)] = ans

        return memo[(i, m)]
