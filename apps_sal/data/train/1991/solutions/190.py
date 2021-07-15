class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        cost = lambda i, j: abs(locations[i] - locations[j])
        
        @lru_cache(maxsize=None)
        def dfs(i, f):
            if f < 0:
                return 0
            total = 0
            if i == finish:
                total += 1
            for j in range(len(locations)):
                if i == j:
                    continue
                total += dfs(j, f - cost(i,j))
            return total
        
        return dfs(start, fuel) % (10**9 + 7)
                

