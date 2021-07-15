class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
\t    cost = lambda i,j: abs(locations[i]-locations[j])
\t    @lru_cache(None)
\t    def dfs(i, f):
\t\t    if f<0: return 0 
\t\t    return sum([dfs(j,f-cost(i,j)) for j in range(len(locations)) if j != i]) + (i==finish)
\t    return dfs(start, fuel) % (10**9+7)

        
