class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        (self.grid, self.lr, self.lc) = (grid, len(grid), len(grid[0]) if grid else 0)
        return max((self.helper(i, j) for i in range(self.lr) for j in range(self.lc) if grid[i][j])) if grid else 0

    def helper(self, x, y):
        nei = [(i, j) for (i, j) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)) if i in range(self.lr) and j in range(self.lc) and self.grid[i][j]]
        (res, val, self.grid[x][y]) = (self.grid[x][y], self.grid[x][y], 0)
        for n in nei:
            res = max(res, self.helper(*n) + val)
        self.grid[x][y] = val
        return res
