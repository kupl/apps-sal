class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        ### start with pos that dosen't have value above
        def dfs(i: int, j: int, visited: List[List[int]]) -> int:
            
            result = grid[i][j]
            for x, y in [[1,0], [0,1], [0,-1], [-1,0]]:
                n_x, n_y = i + x, j+y              
                if 0<=n_x< len(grid) and 0 <= n_y < len(grid[0]) and grid[n_x][n_y] and not visited[n_x][n_y]:
                    visited[n_x][n_y] = 1
                    child = dfs(n_x, n_y, visited)
                    result = max(child + grid[i][j], result)
                    visited[n_x][n_y] = 0
                    
            return result         
        
        total = 0
        
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if (i>0 and i < len(grid)-1 and grid[i-1][j] > 0 and grid[i+1][j] >0) and grid[i][j]:
                    pass                    
                elif grid[i][j]:
                    visited[i][j] = 1 
                    total = max(dfs(i, j, visited), total)
                    visited[i][j] = 0
                    
        
        return total
                    
                    
                    
        
        

