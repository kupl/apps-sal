class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        x = min(m, n)

        right = [[0 for i in range(n)] for j in range(m)]
        down = [[0 for i in range(n)] for j in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    continue

                right[i][j] = 1 + (right[i][j + 1] if j + 1 < n else 0)
                down[i][j] = 1 + (down[i + 1][j] if i + 1 < m else 0)

        for l in range(x, 0, -1):
            for i in range(0, m - l + 1):
                for j in range(0, n - l + 1):
                    if right[i][j] >= l and down[i][j] >= l and right[i + l - 1][j] >= l and down[i][j + l - 1] >= l:
                        return l * l
        return 0
