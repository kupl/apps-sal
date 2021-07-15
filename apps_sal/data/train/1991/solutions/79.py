class Solution:
    def countRoutes(self, A, s: int, e: int, fuel) -> int:
        @lru_cache(None)
        def dfs(i: int, f: int) -> int:
            return 0 if f < 0 else (1 if i == e else 0) + sum(0 if i == j else dfs(j, f - abs(A[j] - A[i])) for j in range(len(A)))
        return dfs(s, fuel) % 1000000007
