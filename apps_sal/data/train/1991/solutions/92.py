class Solution:
    def countRoutes(self, l: List[int], st: int, fin: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(i, f):
            return 0 if f < 0 else (1 if i == fin else 0) + sum(0 if i == j else dfs(j, f - abs(l[i] - l[j])) for j in range(len(l)))
        return dfs(st, fuel) % 1000000007
