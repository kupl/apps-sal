class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7

        @functools.lru_cache(maxsize=None)
        def dp(city: int, tank: int) -> int:
            if tank < 0:
                return 0
            answer = (1 if city == finish else 0)
            for i in range(len(locations)):
                if i != city:
                    answer += dp(i, tank - abs(locations[city] - locations[i]))
                    answer %= MOD
            return answer

        return dp(start, fuel)
