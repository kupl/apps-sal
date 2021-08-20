class Solution:

    def divisorGame(self, N: int) -> bool:
        dp = [False] * (N + 1)
        for i in range(2, N + 1):
            j = 1
            while j < i:
                if i % j == 0 and dp[i - j] == False:
                    dp[i] = True
                    break
                j += 1
        return dp[-1]
