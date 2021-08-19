class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def dist(i, j):
            return abs(locations[i] - locations[j])

        @functools.lru_cache(None)
        def dp(i, fuel):
            if fuel < dist(i, finish):
                return 0
            return sum([dp(j, fuel - dist(i, j)) for j in range(len(locations)) if i != j]) + (i == finish)
        return dp(start, fuel) % (10 ** 9 + 7)
