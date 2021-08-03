class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @functools.lru_cache(None)
        def dp(start, fuel):
            if fuel < 0:
                return 0
            if abs(locations[start] - locations[finish]) > fuel:
                return 0
            return sum([dp(i, fuel - abs(locations[i] - locations[start])) for i in range(len(locations)) if i != start]) + (start == finish)
        return dp(start, fuel) % (10**9 + 7)
