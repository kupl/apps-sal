class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def dp(i, f):
            if i == finish:
                res = 1
            else:
                res = 0
            for j in range(len(locations)):
                if j != i and abs(locations[i] - locations[j]) <= f:
                    res += dp(j, f - abs(locations[i] - locations[j]))
            return res
        return dp(start, fuel) % (10 ** 9 + 7)
