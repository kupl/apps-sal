class Solution:
    def dfs(self, i, j, gold, grid, m, n):
        if 0 <= i < m and 0 <= j < n:
            if grid[i][j] != 0:
                temp = grid[i][j]
                grid[i][j] = 0
                gold = max(self.dfs(x, y, gold + temp, grid, m, n) for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)))
                grid[i][j] = temp
        return gold

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = []
        for i in range(m):
            for j in range(n):
                res.append(self.dfs(i, j, 0, grid, m, n))

        return max(res)
