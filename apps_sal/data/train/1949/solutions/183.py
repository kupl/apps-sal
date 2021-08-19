class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.res = 0
        (m, n) = (len(grid), len(grid[0]))

        def dfs(x, y, visited, cnt):
            if any((0 <= nx < m and 0 <= ny < n and (grid[nx][ny] != 0) and ((nx, ny) not in visited) for (nx, ny) in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]])):
                for (nx, ny) in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                    if 0 <= nx < m and 0 <= ny < n and (grid[nx][ny] != 0) and ((nx, ny) not in visited):
                        dfs(nx, ny, visited | {(nx, ny)}, cnt + grid[nx][ny])
            else:
                self.res = max(self.res, cnt)
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfs(i, j, {(i, j)}, grid[i][j])
        return self.res
