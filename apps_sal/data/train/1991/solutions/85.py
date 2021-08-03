class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def solve(curCity, fuel):
            if fuel < 0:
                return 0
            ans = 1 if curCity == finish else 0
            for nextCity in range(0, len(locations)):
                if nextCity != curCity:
                    ans = (ans + solve(nextCity, fuel - abs(locations[curCity] - locations[nextCity]))) % (1000000007)
            return ans
        return solve(start, fuel)
