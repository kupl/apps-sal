class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        
        @functools.lru_cache(maxsize=None)
        def dp(city: int, tank: int) -> int:
            return ((1 if city == finish else 0) + sum(dp(i, tank - abs(locations[city] - locations[i])) for i in range(len(locations)) if i != city)) % MOD if tank >= 0 else 0
        
        return dp(start, fuel)
