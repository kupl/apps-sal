class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        res = 0
        
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                res = max(res, self.find(grid, i, j))
                
        return res
        
    def find(self, grid, i, j):
        
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or not grid[i][j]:
            return 0
        
        current = grid[i][j]
        
        grid[i][j] = 0
        
        up = self.find(grid, i-1, j)
        down = self.find(grid, i+1, j)
        left = self.find(grid, i, j-1)
        right = self.find(grid, i, j+1)
        
        maxx = max(up, down, left, right)
        grid[i][j] = current
        return maxx + current
