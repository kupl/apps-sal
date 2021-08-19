class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones)
        target = target // 2
        dp = [[False] * (target + 1) for _ in range(len(stones) + 1)]
        for i in range(len(stones) + 1):
            for j in range(target + 1):
                if j == 0:
                    dp[i][j] = True
                elif stones[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - stones[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        for j in reversed(range(target + 1)):
            if dp[-1][j]:
                return sum(stones) - 2 * j
