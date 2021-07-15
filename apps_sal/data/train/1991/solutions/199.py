MOD = 10**9 + 7
class Solution:
    def countRoutes(self, A: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(A)
        
        @lru_cache(None)
        def dfs(i, k):
            res = int(i == finish)
            for j in range(n):
                if i == j:
                    continue
                if abs(A[i] - A[j]) > k:
                    continue
                res += dfs(j, k - abs(A[i] - A[j]))
                res %= MOD
            return res
        
        return dfs(start, fuel)
