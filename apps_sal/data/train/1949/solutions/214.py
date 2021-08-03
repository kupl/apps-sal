class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        seen, n, m = {}, len(grid), len(grid[0])
        maxy, x, y = 0, [1, -1, 0, 0], [0, 0, -1, 1]
        dp = [[0] * m for _ in range(n)]

        def path(i, j, d):
            mm = d
            for k in range(len(x)):
                r, c = i + x[k], j + y[k]
                if 0 <= r < n and 0 <= c < m and grid[r][c] != 0:
                    if (r, c) not in seen or not seen[(r, c)]:
                        seen[(r, c)] = True
                        mm = max(mm, path(r, c, d + grid[r][c]))
                        seen[(r, c)] = False
            return mm

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                seen[(i, j)] = True
                maxy = max(maxy, path(i, j, grid[i][j]))
                seen[(i, j)] = False
        return maxy
