class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.best = 0

        def rec(x, y, total):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] > 0:
                total += grid[x][y]
                self.best = max(self.best, total)
                grid[x][y] = -grid[x][y]
                rec(x - 1, y, total)
                rec(x, y - 1, total)
                rec(x + 1, y, total)
                rec(x, y + 1, total)
                grid[x][y] = abs(grid[x][y])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    rec(r, c, 0)
        return self.best
