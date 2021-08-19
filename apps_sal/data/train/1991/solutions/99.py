class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        (N, R) = (len(locations), 10 ** 9 + 7)
        dp = [[-1] * (fuel + 1) for _ in range(N)]

        def _dfs(p, f):
            if dp[p][f] < 0:
                dp[p][f] = 0
                for q in range(N):
                    if q == p:
                        continue
                    left = f - abs(locations[p] - locations[q])
                    if left < abs(locations[finish] - locations[q]):
                        continue
                    dp[p][f] += _dfs(q, left)
                dp[p][f] += 1 if p == finish else 0
            return dp[p][f] % R
        return _dfs(start, fuel)
