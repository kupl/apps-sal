class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.maxGold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    used = set()
                    self.dfs(i, j, 0, grid, used)
        return self.maxGold

    def dfs(self, i, j, total, grid, used):
        used.add((i, j))
        total += grid[i][j]
        if total > self.maxGold:
            self.maxGold = total
        for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in used and grid[ni][nj] > 0:
                self.dfs(ni, nj, total, grid, used)
        used.remove((i, j))
