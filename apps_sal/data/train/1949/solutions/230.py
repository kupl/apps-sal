class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.grid = None

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        if not len(grid):
            return 0

        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                ans = max(ans, self.dfs(i, j))

        return ans

    def dfs(self, x, y):

        res = 0
        amt = self.grid[x][y]
        self.grid[x][y] = 0

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dx, dy in directions:
            i = x + dx
            j = y + dy
            if i >= 0 and i < self.m and j >= 0 and j < self.n and self.grid[i][j] != 0:
                res = max(res, self.grid[i][j] + self.dfs(i, j))

        self.grid[x][y] = amt

        return res
