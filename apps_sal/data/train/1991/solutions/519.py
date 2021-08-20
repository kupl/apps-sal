sys.setrecursionlimit(1000000)


class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        N = len(locations)
        dp = [[0] * (fuel + 1) for _ in range(N)]
        dp[finish] = [1] * (fuel + 1)
        for f in range(1, fuel + 1):
            for u in range(N):
                for v in range(N):
                    if u != v:
                        delta = abs(locations[u] - locations[v])
                        if delta <= f:
                            dp[u][f] += dp[v][f - delta]
                            dp[u][f] %= MOD
        return dp[start][fuel]
