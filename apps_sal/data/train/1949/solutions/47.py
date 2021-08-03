class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.res = 0
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(i, j, cur, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return

            val = grid[i][j]
            grid[i][j] = 0
            self.res = max(self.res, cur + val)

            for dx, dy in directions:
                dfs(i + dx, j + dy, cur + val, grid)

            grid[i][j] = val

        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    dfs(i, j, 0, grid)
        return self.res
