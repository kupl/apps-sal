class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.ans = 0

        def dfs(x, y, curr):
            curr += grid[x][y]
            self.ans = max(curr, self.ans)
            (temp, grid[x][y]) = (grid[x][y], 0)
            for (nx, ny) in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (grid[nx][ny] != 0):
                    dfs(nx, ny, curr)
            grid[x][y] = temp
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    dfs(i, j, 0)
        return self.ans
