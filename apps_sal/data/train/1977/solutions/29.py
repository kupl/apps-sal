class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        for col in range(n):
            if grid[0][col] == 0:
                self.dfs(0, col, grid)
            if grid[m - 1][col] == 0:
                self.dfs(m - 1, col, grid)
        for row in range(m):
            if grid[row][0] == 0:
                self.dfs(row, 0, grid)
            if grid[row][n - 1] == 0:
                self.dfs(row, n - 1, grid)
        components = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.dfs(i, j, grid)
                    components += 1
        return components

    def dfs(self, i, j, grid):
        grid[i][j] = 1
        stack = [(i, j)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while stack:
            (x, y) = stack.pop()
            for (dx, dy) in directions:
                if x + dx < 0 or y + dy < 0 or x + dx >= len(grid) or (y + dy >= len(grid[0])):
                    continue
                if grid[x + dx][y + dy] == 0:
                    grid[x + dx][y + dy] = 1
                    stack.append((x + dx, y + dy))
