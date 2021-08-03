class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        LU = [[(0, 0)] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    LU[r + 1][c + 1] = (1 + LU[r + 1][c][0], 1 + LU[r][c + 1][1])

        area = 0
        for r in range(m):
            for c in range(n):
                x, y = LU[r + 1][c + 1]
                for i in range(min(x, y) - 1, -1, -1):
                    if min(LU[r + 1 - i][c + 1][0], LU[r + 1][c + 1 - i][1]) >= i + 1:
                        area = max(area, (i + 1)**2)

        return area
