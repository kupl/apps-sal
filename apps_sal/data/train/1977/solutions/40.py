class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        (self.rows, self.cols) = (len(grid), len(grid[0]))
        ans = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 0 and self.dfs(grid, i, j):
                    ans += 1
        return ans

    def dfs(self, grid, row, col):
        if row < 0 or row > self.rows - 1 or col < 0 or (col > self.cols - 1):
            return False
        if grid[row][col] == 1 or grid[row][col] == 2:
            return True
        grid[row][col] = 2
        up = self.dfs(grid, row - 1, col)
        down = self.dfs(grid, row + 1, col)
        left = self.dfs(grid, row, col - 1)
        right = self.dfs(grid, row, col + 1)
        if up and down and left and right:
            return True
        else:
            return False
