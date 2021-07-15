class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        @lru_cache(None)
        def dfs(l, f):
            res = 1 if l == finish else 0
            for i in range(n):
                diff = abs(locations[i] - locations[l])
                if i != l and diff <= f:
                    res += dfs(i, f - diff)
            
            return res
        
        return dfs(start, fuel) % (10 ** 9 + 7)
