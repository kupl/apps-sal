class Solution:
    def countRoutes(self, L: List[int], st: int, fn: int, fuel: int) -> int:
        n = len(L)
        dp = [[0 for i in range(fuel + 1)] for j in range(n)]

        dp[st][fuel] = 1

        for f in range(fuel, -1, -1):
            for u in range(n):
                for v in range(n):
                    if u != v:
                        cost = abs(L[u] - L[v])
                        if f + cost <= fuel:
                            dp[u][f] = dp[u][f] + dp[v][f + cost]
        # print(dp)
        return sum(dp[fn]) % 1000000007
