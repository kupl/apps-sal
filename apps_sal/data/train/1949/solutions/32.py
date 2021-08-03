class Solution:
    def __init__(self):
        self.max = 0

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.max = max(self.dfs(grid, i, j), self.max)

        return self.max

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
            return 0

        temp = grid[i][j]
        grid[i][j] = 0

        up = temp + self.dfs(grid, i - 1, j)
        down = temp + self.dfs(grid, i + 1, j)
        left = temp + self.dfs(grid, i, j - 1)
        right = temp + self.dfs(grid, i, j + 1)

        grid[i][j] = temp
        return max(max(up, down), max(left, right))
