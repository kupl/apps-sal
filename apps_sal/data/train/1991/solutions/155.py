class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def dp(i, j):
            if j < 0:
                return 0
            if i == finish:
                return 1 + sum((dp(k, j - abs(locations[i] - locations[k])) for k in range(len(locations)) if k != i))
            else:
                return sum((dp(k, j - abs(locations[i] - locations[k])) for k in range(len(locations)) if k != i))
        return dp(start, fuel) % (10 ** 9 + 7)
