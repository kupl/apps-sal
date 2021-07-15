class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        m,n = len(grid),len(grid[0])
        
        numIslands = 0
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 0:
                    self.dfs(grid, i, j, 1)
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.dfs(grid, i, j, 1)
                    numIslands += 1
                    
        return numIslands
    
    def dfs(self,grid,i,j,val):
        m,n = len(grid),len(grid[0])
        
        grid[i][j] = val
        for newi,newj in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
            if 0 <= newi < m and 0 <= newj < n and grid[newi][newj] == 0:
                   # grid[newi][newj] = val
                    self.dfs(grid,newi,newj,val)

