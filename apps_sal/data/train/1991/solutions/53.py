class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @functools.lru_cache(None)
        def dp(start , fuel):
            if fuel < 0: return 0
            if abs(locations[start] - locations[finish])> fuel: return 0
            res = 0
            if start == finish:
                res += 1
            for i in range(len(locations)):
                if i!=start:
                    res += dp(i,fuel-abs(locations[i]-locations[start]))
            return res % (10**9+7)
        return dp(start,fuel)

