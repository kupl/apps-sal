class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        horizontal_len = [row[:] for row in grid]
        vertical_len = [row[:] for row in grid]
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    if i > 0:
                        vertical_len[i][j] = vertical_len[i - 1][j] + 1
                    if j > 0:
                        horizontal_len[i][j] = horizontal_len[i][j - 1] + 1

        for width in range(min(m, n), 0, -1):
            for i in range(m - width + 1):
                for j in range(n - width + 1):
                    valid_width = min(horizontal_len[i][j + width - 1],
                                      horizontal_len[i + width - 1][j + width - 1],
                                      vertical_len[i + width - 1][j],
                                      vertical_len[i + width - 1][j + width - 1])
                    if valid_width >= width:
                        return width ** 2
        return 0
