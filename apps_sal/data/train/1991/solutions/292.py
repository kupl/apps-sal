class Solution:
    def countRoutes(self, A: list, start: int, finish: int, fuel: int) -> int:
        n = len(A)
        MOD = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dp(i, k):
            if k < 0:
                return 0
            ans = 1 if i == finish else 0
            for j in range(n):
                if i == j:
                    continue
                ans += dp(j, k - abs(A[i] - A[j]))
            return ans % MOD

        return dp(start, fuel)
