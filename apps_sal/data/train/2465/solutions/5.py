class Solution:

    def divisorGame(self, N: int) -> bool:
        dp = [False for i in range(N + 1)]
        for i in range(N + 1):
            for x in range(1, i // 2 + 1):
                if i % x == 0 and (not dp[i - x]):
                    dp[i] = True
                    break
        return dp[N]
