class Solution:

    def maxgold(self, grid, i, j, visited={}):
        # search for max gold path from i,j
        if 0 <= i and i < len(grid) and j >= 0 and j < len(grid[0]):
            # print((i,j))
            if (i, j) not in visited or visited[(i, j)] == 0:
                visited[(i, j)] = 1
                if grid[i][j] != 0:
                    value = grid[i][j] + max(self.maxgold(grid, i + 1, j, visited), self.maxgold(grid, i - 1, j, visited), self.maxgold(grid, i, j + 1, visited), self.maxgold(grid, i, j - 1, visited))
                    visited[(i, j)] = 0
                    return value

        return 0

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # at each grid[i][j] such that

        val = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    # do a search starting from grid[i][j]
                    # print(self.maxgold(grid,i,j, {}))
                    if self.maxgold(grid, i, j, {}) > val:
                        val = self.maxgold(grid, i, j, {})

        return val
