class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @functools.lru_cache(None)
        def dp(city, left):
            if left < 0:
                return 0
            return (1 if city==finish else 0) + sum([dp(dest, left-abs(locations[dest]-locations[city]))\\
                for dest in range(len(locations)) if dest!=city])%(10**9+7)
        return dp(start, fuel)
