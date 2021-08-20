class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        ln = len(locations)
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dp(cur, fuel):
            if fuel < 0:
                return 0
            ans = 1 if cur == finish else 0
            for city in range(ln):
                if city != cur:
                    ans += dp(city, fuel - abs(locations[city] - locations[cur]))
                    ans %= mod
            return ans
        return dp(start, fuel)
