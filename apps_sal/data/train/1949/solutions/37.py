DIR = ((-1, 0), (1, 0), (0, -1), (0, 1))


class Solution:
    def getMaximumGold(self, grid):
        res = 0
        m, n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y] > 0:
                    res = max(res, self.dfs(grid, x, y, {(x, y)}))
        return res

    def dfs(self, grid, x, y, visited):
        m, n = len(grid), len(grid[0])
        res = grid[x][y]
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= m - 1 and 0 <= ny <= n - 1 and grid[nx][ny] > 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                res = max(res, self.dfs(grid, nx, ny, visited) + grid[x][y])
                visited.remove((nx, ny))
        return res
