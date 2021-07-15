class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        def cost(i, j):
            return abs(locations[i]-locations[j])
        
        @lru_cache(None)
        def dfs(i, fuel):
            if fuel < 0:
                return 0
            ans = 0
            if finish == i:
                ans += 1
                
            for j in range(len(locations)):
                if i == j:
                    continue
                ans += (dfs(j, fuel-cost(i, j)))
                
            return ans
        
        return dfs(start, fuel) % (10**9+7)
