class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        maxGold = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            res = 0
            if grid[i][j] == 0:
                return 0
            tmp = grid[i][j]
            grid[i][j] = 0
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < m and 0 <= y < n:
                    res = max(res, dfs(x, y))

            grid[i][j] = tmp
            return res + grid[i][j]

        for i in range(m):
            for j in range(n):
                maxGold = max(maxGold, dfs(i, j))

        return maxGold
