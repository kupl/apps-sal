class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        top = [a[:] for a in grid]
        left = [a[:] for a in grid]

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i > 0:
                        top[i][j] = top[i - 1][j] + 1
                    if j > 0:
                        left[i][j] = left[i][j - 1] + 1

        for r in range(min(m, n), 0, -1):
            for i in range(m - r + 1):
                for j in range(n - r + 1):
                    if min(top[i + r - 1][j], top[i + r - 1][j + r - 1], left[i][j + r - 1], left[i + r - 1][j + r - 1]) >= r:
                        return r * r

        return 0
