class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(maxsize=None)
        def count(start: int, fuel: int, MOD=10**9 + 7) -> int:
            if fuel < 0:
                return 0
            elif fuel == 0 and start == finish:
                return 1
            else:
                ways = 1 if start == finish else 0
                for i, loc in enumerate(locations):
                    if i != start:
                        ways = (ways + count(i, fuel - abs(loc - locations[start]))) % MOD
                return ways

        return count(start, fuel)
