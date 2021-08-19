class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        (N, R) = (len(locations), 10 ** 9 + 7)
        dp = [[-1] * (fuel + 1) for _ in range(N)]

        def _dfs(p, f):
            cost = abs(locations[finish] - locations[p])
            if cost > f:
                return 0
            if dp[p][f] < 0:
                dp[p][f] = sum((_dfs(q, f - abs(locations[p] - locations[q])) for q in range(N) if q != p))
                dp[p][f] += 1 if p == finish else 0
            return dp[p][f] % R
        return _dfs(start, fuel)
