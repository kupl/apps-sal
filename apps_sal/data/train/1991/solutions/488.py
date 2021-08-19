class Solution:

    def countRoutes(self, loc: List[int], start: int, end: int, fuel: int) -> int:
        n = len(loc)
        m = int(1000000000.0 + 7)
        dp = [[0 for _ in range(fuel + 1)] for _ in range(n)]
        for f in range(fuel + 1):
            dp[end][f] = 1
        for f in range(1, fuel + 1):
            for i in range(n):
                for j in range(i + 1, n):
                    a = abs(loc[i] - loc[j])
                    if a <= f:
                        dp[i][f] = (dp[i][f] + dp[j][f - a]) % m
                        dp[j][f] = (dp[j][f] + dp[i][f - a]) % m
        return dp[start][fuel]
