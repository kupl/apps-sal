class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def dp(i, f):
            if f < 0:
                return 0
            return (sum((dp(j, f - abs(locations[i] - locations[j])) for j in range(len(locations)) if i != j)) + (i == finish)) % (10 ** 9 + 7)
        return dp(start, fuel)
