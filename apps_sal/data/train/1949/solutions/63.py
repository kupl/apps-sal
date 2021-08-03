class Solution(object):
    def getMaximumGold(self, grid):

        self.ans = 0

        def helper(grid, i, j, s):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
                tmp = grid[i][j]
                grid[i][j] = 0
                helper(grid, i + 1, j, s + tmp)
                helper(grid, i - 1, j, s + tmp)
                helper(grid, i, j + 1, s + tmp)
                helper(grid, i, j - 1, s + tmp)
                grid[i][j] = tmp

            else:
                self.ans = max(self.ans, s)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    helper(grid, i, j, 0)

        return self.ans
