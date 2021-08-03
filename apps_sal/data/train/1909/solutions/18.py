class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0

        up = [[0] * n for _ in range(m)]
        left = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    up[i][j] = 1 + (up[i - 1][j] if i > 0 else 0)
                    left[i][j] = 1 + (left[i][j - 1] if j > 0 else 0)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    down[i][j] = 1 + (down[i + 1][j] if i + 1 < m else 0)
                    right[i][j] = 1 + (right[i][j + 1] if j + 1 < n else 0)

        print(up)
        print(left)
        print(down)
        print(right)

        ans = -1
        for i in range(m):
            for j in range(n):
                min_1 = min(up[i][j], left[i][j])
                for k in range(min_1):
                    if min(down[i - k][j - k], right[i - k][j - k]) >= k:
                        ans = max(ans, k)

        return (ans + 1)**2
