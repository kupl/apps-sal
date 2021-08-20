import functools


class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @functools.lru_cache(None)
        def doit(start, fuel):
            if fuel < 0:
                return 0
            ans = 0
            if start == finish and fuel >= 0:
                ans += 1
            for i in range(len(locations)):
                if i != start and fuel >= abs(locations[i] - locations[start]):
                    ans += doit(i, fuel - abs(locations[i] - locations[start]))
            return ans % 1000000007
        return doit(start, fuel)
