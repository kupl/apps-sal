class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])

        def dfs(x, y, gold):
            temp = grid[x][y]
            grid[x][y] = 0
            self.max_gold = max(self.max_gold, gold + temp)
            for dx, dy in dirs:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                    dfs(nx, ny, gold + temp)
            grid[x][y] = temp

        self.max_gold = 0
        for i in range(m):
            for j in range(n):
                dfs(i, j, 0)
        return self.max_gold
