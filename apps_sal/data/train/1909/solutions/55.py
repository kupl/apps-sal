class Solution:

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        (n, m) = (len(grid), len(grid[0]))
        (right, below) = ([[0] * m for i in range(n)], [[0] * m for i in range(n)])
        for i in range(n):
            for j in range(m):
                if i == 0:
                    below[n - 1 - i][m - 1 - j] = grid[n - 1 - i][m - 1 - j]
                else:
                    below[n - 1 - i][m - 1 - j] = grid[n - 1 - i][m - 1 - j] * (1 + below[n - i][m - 1 - j])
                if j == 0:
                    right[n - 1 - i][m - 1 - j] = grid[n - 1 - i][m - 1 - j]
                else:
                    right[n - 1 - i][m - 1 - j] = grid[n - 1 - i][m - 1 - j] * (1 + right[n - 1 - i][m - j])
        max_s = 0
        for i in range(n):
            for j in range(n - i):
                for k in range(m - j):
                    if (below[i][k] >= j + 1) & (right[i][k] >= j + 1):
                        if (below[i][k + j] >= j + 1) & (right[i + j][k] >= j + 1):
                            if j + 1 > max_s:
                                max_s = j + 1
        return max_s ** 2
