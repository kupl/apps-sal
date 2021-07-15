class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 or row == len(grid)-1 or col == 0 or col == len(grid[0])-1:
                    if grid[row][col] == 0:
                        self.dfs(grid, row, col)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    islands += 1
                    self.dfs(grid, row, col)

        return islands


    def dfs(self, grid, row, col):
        grid[row][col] = 1

        for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= row + i < len(grid) and 0 <= col + j < len(grid[0]):
                if grid[row+i][col+j] == 0:
                    self.dfs(grid, row+i, col+j)

