class Solution:
    def divisorGame(self, N: int) -> bool:
        if N <= 1:
            return False
        dp = [False] * (N + 1)
        for i in range(2, N + 1):
            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    nextN = i - j
                    if dp[nextN] == False:
                        dp[i] = True

        return dp[N]
