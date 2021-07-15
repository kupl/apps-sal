class Solution:
    def countRoutes(self, loct: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(loct)
        def getf(s,e):
            return abs(loct[s] - loct[e])
        visited = set()
        @functools.lru_cache(None)
        def dfs(start, f): 
            if f < 0:
                return 0
            return sum([dfs(i, f - getf(start, i)) for i in range(n) if i != start]) + (1 if start == finish else 0)
        return dfs(start, fuel) % (10 **9 + 7)
