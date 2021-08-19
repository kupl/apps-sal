class Solution:
    def dfs(self, grid, i, j):
        if (i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[0])) or (grid[i][j] == 0):
            return 0

        temp = grid[i][j]
        grid[i][j] = 0

        max_gold = temp + max(
            self.dfs(grid, i + 1, j),
            self.dfs(grid, i - 1, j),
            self.dfs(grid, i, j + 1),
            self.dfs(grid, i, j - 1))
        grid[i][j] = temp
        return max_gold

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                max_gold = self.dfs(grid, i, j)
                # print(\"max gold: \", max_gold)
                res = max(res, max_gold)
        return res
