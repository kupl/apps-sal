class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        diff = total
        dp = [[False] * (1 + total) for _ in range(1 + n)]
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            s = stones[i - 1]
            for j in range(1, 1 + total):
                if j < s:
                    dp[i][j] = dp[i - 1][j]
                    continue
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - s]
                if dp[i][j]:
                    diff = min(diff, abs(total - 2 * j))
        return diff
