class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False, False]
        for x in range(2, N+1):
            dp.append(any([not dp[x-i] for i in range(1, int(math.sqrt(x))+1) if x % i == 0]))
        return dp[-1]
