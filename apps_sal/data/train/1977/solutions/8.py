class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        closed_island = 0
        if not grid:
            return closed_island

        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                if grid[r][c] == 0 and self.dfs(grid, r, c):
                    closed_island += 1

        return closed_island

    def dfs(self, grid, i, j):

        if grid[i][j] == 1:
            return True

        if i <= 0 or j <= 0 or i >= len(grid) - 1 or j >= len(grid[0]) - 1:
            return False

        grid[i][j] = 1

        top = self.dfs(grid, i - 1, j)
        bottom = self.dfs(grid, i + 1, j)
        left = self.dfs(grid, i, j - 1)
        right = self.dfs(grid, i, j + 1)

        return top and left and right and bottom
