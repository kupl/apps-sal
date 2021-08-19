class Solution:

    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        elif N == 2:
            return True
        dp = [False] * (N + 1)
        dp[1] = True
        dp[2] = True
        for i in range(3, N + 1):
            for j in range(1, i):
                if i % 2 == 0:
                    dp[i] = True
                    break
        print(dp)
        return dp[-1]
