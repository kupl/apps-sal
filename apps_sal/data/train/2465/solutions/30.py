class Solution:

    def divisorGame(self, N: int) -> bool:
        if N < 2:
            return False
        dp = [False] * (N + 1)
        dp[2] = True
        for i in range(2, N + 1):
            for x in range(1, i):
                if i % x == 0 and (not dp[i - x]):
                    dp[i] = True
        return dp[-1]
