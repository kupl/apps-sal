class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def backtrack(grid, i, j):
            s = 0
            temp = grid[i][j]
            grid[i][j] = 0

            # left
            if i > 0 and grid[i - 1][j] != 0:
                s = max(s, backtrack(grid, i - 1, j))

            # right
            if i < len(grid) - 1 and grid[i + 1][j] != 0:
                s = max(s, backtrack(grid, i + 1, j))

            # top
            if j > 0 and grid[i][j - 1] != 0:
                s = max(s, backtrack(grid, i, j - 1))

            # bottom
            if j < len(grid[0]) - 1 and grid[i][j + 1] != 0:
                s = max(s, backtrack(grid, i, j + 1))

            grid[i][j] = temp
            return s + grid[i][j]

        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    ret = max(ret, backtrack(grid, i, j))
        return ret
