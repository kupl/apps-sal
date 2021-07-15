class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_g = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 0):
                    continue
                max_g = max(max_g,self.dfs(i,j,grid))
        return max_g
                
    def dfs(self, i, j, grid):
        if(i < 0 or j<0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0):
            return 0
        temp = grid[i][j]
        grid[i][j] = 0
        res = 0
        for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            res = max(res, temp+self.dfs(i+di,j+dj,grid))
        grid[i][j] = temp
        return res
