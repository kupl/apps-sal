class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def dfs(k, f):
            res = 1 if k == finish else 0
            for i in range(n):
                if i != k and dist[i][k] <= f:
                    res += dfs(i, f - dist[i][k])
                    res %= mod
            return res
        n = len(locations)
        mod = 10 ** 9 + 7
        dist = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dist[i][j] = abs(locations[i] - locations[j])
                dist[j][i] = dist[i][j]
        return dfs(start, fuel)
