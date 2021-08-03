class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        m = 10**9 + 7

        @lru_cache(None)
        def dfs(s, e, f):
            if f < 0:
                return 0
            res = 1 if s == e else 0
            for l in locations:
                if l != s:
                    res += dfs(l, e, f - abs(l - s))
            return res % m
        return dfs(locations[start], locations[finish], fuel)
