class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def helper(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            val = grid[i][j]
            grid[i][j] = 0
            res = val + max(helper(i + 1, j), helper(i - 1, j), helper(i, j + 1), helper(i , j - 1))
            grid[i][j] = val
            return res
        self.res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    self.res = max(self.res, helper(i, j))
        return self.res
