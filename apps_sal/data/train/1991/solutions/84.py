class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        R = 10 ** 9 + 7
        N = len(locations)

        @functools.lru_cache(maxsize=None)
        def dp(i, fuel):
            res = 1 if i == finish else 0
            for j in range(N):
                if j != i:
                    cost = abs(locations[i] - locations[j])
                    if fuel >= cost:
                        res = (res + dp(j, fuel - cost)) % R
            return res
        return dp(start, fuel)
