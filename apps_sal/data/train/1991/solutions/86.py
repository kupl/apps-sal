sys.setrecursionlimit(1000000)


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        start, finish = locations[start], locations[finish]
        if abs(finish - start) > fuel:
            return 0
        locations = [x for x in locations if abs(x - start) <= fuel]

        @lru_cache(None)
        def dfs(u, fuel):
            res = 1 if u == finish else 0
            for v in locations:
                if v != u:
                    cost = abs(v - u)
                    if cost <= fuel:
                        res += dfs(v, fuel - cost)
            return res % MOD

        return dfs(start, fuel)
