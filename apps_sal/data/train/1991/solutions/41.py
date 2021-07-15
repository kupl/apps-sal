class Solution:
    def countRoutes(self, A: List[int], start: int, finish: int, fuel: int) -> int:
        n, mod = len(A), 10 ** 9 + 7
        @functools.lru_cache(None)
        def dfs(i, f):
            ret = 1 if i == finish else 0
            for j in range(n):
                if i != j and abs(A[i] - A[j]) <= f:
                    ret += dfs(j, f - abs(A[i] - A[j]))
            return ret
        return dfs(start, fuel) % mod
