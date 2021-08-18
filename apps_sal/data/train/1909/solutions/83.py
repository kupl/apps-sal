class Solution:
    def largest1BorderedSquare(self, grid):
        n = len(grid)
        m = len(grid[0])
        rows = [[0 for j in range(m + 1)] for i in range(1 + n)]
        cols = [[0 for j in range(m + 1)] for i in range(1 + n)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                rows[i][j] = rows[i][j - 1] + grid[i - 1][j - 1]
                cols[i][j] = cols[i - 1][j] + grid[i - 1][j - 1]
        res = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if grid[i - 1][j - 1]:
                    k = 1
                    res = max(res, 1)
                    while i + k <= n and j + k <= m:
                        if rows[i][j + k] - rows[i][j - 1] == rows[i + k][j + k] - rows[i + k][j - 1] == cols[i + k][j] - cols[i - 1][j] == cols[i + k][j + k] - cols[i - 1][j + k] == k + 1:
                            res = max(res, (k + 1) * (k + 1))
                        k += 1
        return res
