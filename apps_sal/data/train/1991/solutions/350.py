sys.setrecursionlimit(1000000)


class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(u, fuel):
            res = 1 if u == finish else 0
            du = locations[u]
            for (v, dv) in enumerate(locations):
                if v != u:
                    cost = abs(dv - du)
                    if cost <= fuel:
                        res += dfs(v, fuel - cost)
            return res % MOD
        return dfs(start, fuel)
