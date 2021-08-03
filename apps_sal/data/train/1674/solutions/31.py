MIN = float('-inf')


class Solution:
    def stoneGameII(self, piles):

        n = len(piles)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] += preSum[i - 1] + piles[i - 1]

        def dfs(start, M, memo):
            if start == n:
                return 0
            if (start, M) in memo:
                return memo[(start, M)]
            max_diff = MIN
            for X in range(1, 2 * M + 1):
                end = min(n, start + X)
                cur = preSum[end] - preSum[start]
                max_diff = max(max_diff, cur - dfs(end, max(M, X), memo))
            memo[(start, M)] = max_diff
            return max_diff

        total = sum(piles)
        return (dfs(0, 1, {}) + total) // 2
