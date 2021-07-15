class Solution:\r
    LAND = 0\r
    WATER = 1\r
    def closedIsland(self, grid: List[List[int]]) -> int:\r
        if not grid:\r
            return 0\r
        count=0\r
        m, n, count = len(grid), len(grid[0]) if grid else 0, 0           \r
        for i in range(1, len(grid)-1):\r
            for j in range(1, len(grid[0])-1):\r
                if grid[i][j]==self.LAND and self.dfs(i,j,grid) :\r
                 count +=1\r
        return count\r
    def inside_grid(self,x, y,grid):\r
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])\r
    \r
    def dfs(self,i,j,grid):\r
        #m, n = len(grid), len(grid[0]) if grid else 0       \r
        #Test = True\r
        if grid[i][j]==self.WATER:\r
            Test = True\r
            return True\r
        \r
        if(i<=0 or j<=0 or j>= len(grid[0])-1 or i >= len(grid)-1):\r
            Test = False\r
            return False\r
        grid[i][j] = self.WATER \r
        Test= True & self.dfs(i+1,j,grid)\r
        Test= Test& self.dfs(i-1,j,grid)\r
        Test= Test& self.dfs(i,j+1,grid)\r
        Test= Test& self.dfs(i,j-1,grid)\r
        return Test  \r
# c= Solution()\r
# grid=[[1,1,0,1,1,1,1,1,1,1],[0,0,1,0,0,1,0,1,1,1],[1,0,1,0,0,0,1,0,1,0],[1,1,1,1,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,0],[0,0,0,0,1,1,0,0,0,0],[1,0,1,0,0,0,0,1,1,0],[1,1,0,0,1,1,0,0,0,0],[0,0,0,1,1,0,1,1,1,0],[1,1,0,1,0,1,0,0,1,0]]\r
# grid2=[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]\r
# c.closedIsland(grid)
