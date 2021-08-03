class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        elif N == 2:
            return True

        dp = [False for _ in range(N + 1)]
        dp[2] = True

        for a in range(3, N + 1):
            for b in range(1, a):
                if a % b == 0 and dp[a - b] == False:
                    dp[a] = True
                    break

        return dp[-1]
