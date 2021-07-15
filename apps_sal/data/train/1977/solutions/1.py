class Solution:
    LAND = 0
    WATER = 1
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        count=0
        m, n, count = len(grid), len(grid[0]) if grid else 0, 0           
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j]==self.LAND and self.dfs(i,j,grid) :
                    count +=1
        return count
    def inside_grid(self,x, y,grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    def dfs(self,i,j,grid):
        #m, n = len(grid), len(grid[0]) if grid else 0       
        #Test = True
        if grid[i][j]==self.WATER:
            Test = True
            return True
        
        if(i<=0 or j<=0 or j>= len(grid[0])-1 or i >= len(grid)-1):
            Test = False
            return False
        grid[i][j] = self.WATER 
        Test= True & self.dfs(i+1,j,grid)
        Test= Test& self.dfs(i-1,j,grid)
        Test= Test& self.dfs(i,j+1,grid)
        Test= Test& self.dfs(i,j-1,grid)
        return Test  
