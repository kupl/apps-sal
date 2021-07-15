class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.dfs(grid, i, j, 0)
        return self.res
        
    def dfs(self, grid, i, j, currSum):
        if i > len(grid) - 1 or i < 0 or j > len(grid[0])-1 or j < 0:
            return 
        if grid[i][j] == 0:
            return
        currSum += grid[i][j]
        temp = grid[i][j]
        grid[i][j] = 0
        self.dfs(grid, i-1, j, currSum)
        self.dfs(grid, i, j-1, currSum)
        self.dfs(grid, i+1, j, currSum)
        self.dfs(grid, i, j+1, currSum)
        grid[i][j] = temp
        self.res = max(self.res, currSum)
