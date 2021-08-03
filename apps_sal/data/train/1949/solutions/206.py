class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j, total, visited):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0 or (i, j) in visited:
                return
            nonlocal ma
            total = total + grid[i][j]
            ma = max(ma, total)
            dfs(i + 1, j, total, visited + [(i, j)])
            dfs(i - 1, j, total, visited + [(i, j)])
            dfs(i, j + 1, total, visited + [(i, j)])
            dfs(i, j - 1, total, visited + [(i, j)])

        c = -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ma = 0
                    dfs(i, j, 0, [])
                    c = max(c, ma)

        return c
