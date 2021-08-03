from functools import lru_cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9 + 7

        @lru_cache(maxsize=None)
        def dfs(i, fuel):
            total = 1 if i == finish else 0
            if fuel < 0:
                return 0
            for j in range(len(locations)):
                if j != i:
                    leftFuel = fuel - abs(locations[i] - locations[j])
                    total += dfs(j, leftFuel)
                    total = total % mod
            return total
        return dfs(start, fuel)
