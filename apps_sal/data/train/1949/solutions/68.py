class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        mx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                mx = max(mx, self.helper(grid, i, j))
        return mx
    
    def helper(self, grid, i, j):
        if grid[i][j] == 0:
            return 0
        res = grid[i][j]
        newGrid = [row.copy() for row in grid]
        newGrid[i][j] = 0
        up, down, left, right = 0, 0, 0, 0
        if i-1 >= 0:
            up = self.helper(newGrid, i-1, j)
        if i+1 < len(grid):
            down = self.helper(newGrid, i+1, j)
        if j-1 >= 0:
            left = self.helper(newGrid, i, j-1)
        if j+1 < len(grid[0]):
            right = self.helper(newGrid, i, j+1)
        res += max(up, down, left, right)
        return res
