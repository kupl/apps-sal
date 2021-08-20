class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        (self.rows, self.cols) = (len(grid), len(grid[0]))
        self.memo = {}
        ans = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 0:
                    ans += self.dfs(grid, row, col)
        return ans

    def dfs(self, grid, row, col):
        if row < 0 or row > self.rows - 1 or col < 0 or (col > self.cols - 1):
            return False
        if (row, col) in self.memo:
            return self.memo[row, col]
        if grid[row][col] == 1:
            return True
        elif row == 0 or row == self.rows - 1 or col == 0 or (col == self.cols - 1):
            return False
        flag = True
        directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        grid[row][col] = 1
        for i in range(4):
            (r, c) = directions[i]
            flag = flag and self.dfs(grid, r, c)
        self.memo[row, col] = flag
        return self.memo[row, col]
