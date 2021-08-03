class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dp(i, left):
            if left < 0:
                return 0
            ret = i == finish
            for ni in range(len(locations)):
                if i == ni:
                    continue
                ret += dp(ni, left - abs(locations[i] - locations[ni]))
            return ret
        return dp(start, fuel) % (10**9 + 7)
