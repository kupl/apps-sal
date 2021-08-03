class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        edge, m, n = 0, len(grid), len(grid[0])
        left, top = [[0 for j in range(n + 1)] for i in range(m + 1)], [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                left[i + 1][j + 1] = (0 if grid[i][j] == 0 else 1 + left[i + 1][j])
                top[i + 1][j + 1] = (0 if grid[i][j] == 0 else 1 + top[i][j + 1])
                left_ones, top_one = left[i + 1][j + 1], top[i + 1][j + 1]
                for length in range(min(left_ones, top_one), edge, -1):
                    if min(left[i + 2 - length][j + 1], top[i + 1][j + 2 - length]) >= length:
                        edge = max(edge, length)
                        break
        return edge**2
