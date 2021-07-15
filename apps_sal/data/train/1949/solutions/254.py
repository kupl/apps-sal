class Solution:
        
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        if not len(grid):
            return 0
        
        grid = grid
        m = len(grid)
        n = len(grid[0])
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans,self.dfs(i,j,grid))
                
        return ans
                
        
        
    def dfs(self,x,y,grid):
        
        amt = grid[x][y]
        res = 0
        grid[x][y] = 0
        
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        for dx,dy in directions:
            i = x + dx
            j = y + dy
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] != 0:
                res = max(res,self.dfs(i,j,grid))
        
        grid[x][y] = amt        
        res += amt
        
        return res
        

