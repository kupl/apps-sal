class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(locations)

        @lru_cache(None)
        def dp(i, k):
            if k < 0:
                return 0
            ans = 1 if i == finish else 0
            for j in range(N):
                if i == j:
                    continue
                ans += dp(j, k - abs(locations[i] - locations[j]))
            ans %= 1000000007
            return ans
        return dp(start, fuel)
