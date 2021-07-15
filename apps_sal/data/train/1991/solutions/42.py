class Solution:
    def countRoutes(self, locs: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(i: int, f: int) -> int:
            res = 1 if i == finish else 0
            for j in range(len(locs)):
                if i != j and f >= abs(locs[j] - locs[i]):
                    res += dfs(j, f - abs(locs[j] - locs[i]))
            return res % 1000000007
        return dfs(start, fuel)
