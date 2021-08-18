class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False for _ in range(N + 1)]

        for i in range(N + 1):
            for j in range(1, i // 2 + 1):
                if i % j == 0 and dp[i - j] == False:
                    dp[i] = True

        return dp[-1]
