class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        result = [float('-inf')]
        
        m, n = len(grid), len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):                
                self.backtrack(grid, i, j, m, n, visited, result, 0)
                        
        return result[0]
    
    
    def isValid(self, grid, i, j, m, n, vis):
        return 0 <= i < m and 0 <= j < n and grid[i][j] != 0 and vis[i][j] == False
    
    
    def backtrack(self, grid, i, j, m, n, vis, result, ttl):
        if self.isValid(grid, i, j, m, n, vis):
            newttl = ttl + grid[i][j]
            
            result[0] = max(result[0], newttl)
            # newVis = vis.copy()
            vis[i][j] = True
            
            
            # Up
            self.backtrack(grid, i-1, j, m, n, vis, result, newttl)
            
            # Left
            self.backtrack(grid, i, j-1, m, n, vis, result, newttl)
            
            # Bottom
            self.backtrack(grid, i+1, j, m, n, vis, result, newttl)
            
            # Right
            self.backtrack(grid, i, j+1, m, n, vis, result, newttl)
            
            vis[i][j] = False
