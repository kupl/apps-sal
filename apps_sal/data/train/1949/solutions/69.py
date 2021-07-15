import copy
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.max = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] != 0:
                    self.helper(grid, i, j, 0)
        return self.max
        
    def helper(self, grid, i, j, goldCount):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            self.max = max(self.max, goldCount)
            return
        goldCount += grid[i][j]
        val = grid[i][j]
        grid[i][j] = 0
        self.helper(grid, i+1, j, goldCount)
        self.helper(grid, i-1, j, goldCount)
        self.helper(grid, i, j+1, goldCount)
        self.helper(grid, i, j-1, goldCount)
        grid[i][j] = val
