class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        (m, n) = (len(grid), len(grid[0]))

        def dfs(i, j, g, c):
            if 0 <= i < m and 0 <= j < n and (grid[i][j] != 0):
                c += grid[i][j]
                tmp = grid[i][j]
                grid[i][j] = 0
                res = max(dfs(i + 1, j, g, c), dfs(i - 1, j, g, c), dfs(i, j + 1, g, c), dfs(i, j - 1, g, c))
                grid[i][j] = tmp
                return res
            else:
                return c
            return c
        x = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    c = 0
                    x.append(dfs(i, j, grid, c))
        return max(x)
