class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.ans = 0

        def dfs(grid, i, j, res):
            res = res + grid[i][j]
            tmp = grid[i][j]
            grid[i][j] = 0
            for (r, c) in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    if grid[r][c]:
                        dfs(grid, r, c, res)
            grid[i][j] = tmp
            self.ans = max(self.ans, res)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]:
                    dfs(grid, i, j, 0)
        return self.ans
