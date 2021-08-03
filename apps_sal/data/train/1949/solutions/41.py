class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = [0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] > 0):
                    self.dfs(grid, i, j, [], ans)
        return ans[0]

    def dfs(self, grid, i, j, path, ans):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return
        path.append(grid[i][j])
        grid[i][j] = 0
        ans[0] = max(ans[0], sum(path))
        self.dfs(grid, i + 1, j, path, ans)
        self.dfs(grid, i - 1, j, path, ans)
        self.dfs(grid, i, j + 1, path, ans)
        self.dfs(grid, i, j - 1, path, ans)
        grid[i][j] = path.pop()
