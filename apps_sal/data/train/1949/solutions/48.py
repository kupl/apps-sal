class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        (m, n) = (len(grid), len(grid[0]))
        res = [0]

        def bfs(v, x, y):
            seen.add((x, y))
            dp[x][y] = max(dp[x][y], v)
            for (i, j) in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                (a, b) = (x + i, y + j)
                if 0 <= a < m and 0 <= b < n and ((a, b) not in seen) and (grid[a][b] != 0):
                    bfs(v + grid[a][b], a, b)
            seen.discard((x, y))
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    seen = set()
                    bfs(grid[i][j], i, j)
        return max((max(row) for row in dp))
