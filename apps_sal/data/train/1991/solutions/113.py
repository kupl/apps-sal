class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(locations)
        mod = 1000000007

        @lru_cache(None)
        def dfs(city, fuel):
            c = int(city == finish)
            for i in range(N):
                if i != city:
                    cost = abs(locations[i] - locations[city])
                    if cost <= fuel:
                        c = (c + dfs(i, fuel - cost)) % mod
            return c

        return dfs(start, fuel)
