class Solution:

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        (m, n) = (len(grid), len(grid[0]))
        left = [a[:] for a in grid]
        top = [a[:] for a in grid]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    left[i][j] = left[i][j - 1] + 1 if j else 1
                    top[i][j] = top[i - 1][j] + 1 if i else 1
        for l in range(min(m, n), 0, -1):
            for i in range(m - l + 1):
                for j in range(n - l + 1):
                    if min(top[i + l - 1][j], top[i + l - 1][j + l - 1], left[i][j + l - 1], left[i + l - 1][j + l - 1]) >= l:
                        return l * l
        return 0
