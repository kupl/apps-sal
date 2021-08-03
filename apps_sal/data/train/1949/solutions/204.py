class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c, total, vis):
            nonlocal maxx
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or (r, c) in vis:
                return
            total += grid[r][c]
            maxx = max(total, maxx)
            dfs(r + 1, c, total, vis + [(r, c)])
            dfs(r - 1, c, total, vis + [(r, c)])
            dfs(r, c + 1, total, vis + [(r, c)])
            dfs(r, c - 1, total, vis + [(r, c)])

        grt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    maxx = 0
                    dfs(i, j, 0, [])
                    grt = max(grt, maxx)
        return grt
