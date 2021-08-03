class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        self.maxResult = float('-inf')
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] > 0:
                    self._getMaxGoldHelper(grid, r, c, 0)
        return self.maxResult

    def _getMaxGoldHelper(self, grid, r, c, currSum):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] <= 0:
            return
        currSum += grid[r][c]
        self.maxResult = max(self.maxResult, currSum)
        grid[r][c] *= -1
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self._getMaxGoldHelper(grid, r + dir[0], c + dir[1], currSum)
        grid[r][c] *= -1
