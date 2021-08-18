class Solution:
    def countRoutes(self, A: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(A)
        MOD = 10**9 + 7

        @functools.lru_cache(None)
        def dp(i, rem):
            if rem == 0:
                return 0
            ways = 0
            for j in range(N):
                deltaF = rem - abs(A[i] - A[j])
                if i != j and deltaF >= 0:
                    ways = (ways + dp(j, deltaF)) % MOD
                    if j == finish:
                        ways = (ways + 1) % MOD
            return ways
        return dp(start, fuel) + (1 if start == finish else 0)
