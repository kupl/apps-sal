class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        kMod = 1e9+7
        @lru_cache(None)
        def dp(i, f):
            if (f < 0): return 0
            # if (i == finish): return 1
            
            return (sum([dp(j, f - abs(locations[j] - locations[i])) for j in range(n) if j != i]) + (i==finish))%kMod
        return int(dp(start, fuel))

