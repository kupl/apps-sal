class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)

        @lru_cache(maxsize=None)
        def dp(cur, finish, fuel):
            if fuel < 0:
                return 0
            ans = 1 if cur == finish else 0
            for (nextCity, val) in enumerate(locations):
                if nextCity != cur:
                    ans += dp(nextCity, finish, fuel - abs(val - locations[cur]))
            return ans % (10 ** 9 + 7)
        return dp(start, finish, fuel)
