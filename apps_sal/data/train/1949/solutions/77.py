class Solution:
    def dfs(self, cur_gold, max_gold, grid, visited, i, j):
        if (i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[0])) or (visited[i][j] == 1) or (grid[i][j] == 0):
            return
        visited[i][j] = 1
        self.dfs(cur_gold + grid[i][j], max_gold, grid, visited, i + 1, j)
        self.dfs(cur_gold + grid[i][j], max_gold, grid, visited, i - 1, j)
        self.dfs(cur_gold + grid[i][j], max_gold, grid, visited, i, j + 1)
        self.dfs(cur_gold + grid[i][j], max_gold, grid, visited, i, j - 1)
        max_gold[0] = max(max_gold[0], cur_gold + grid[i][j])
        visited[i][j] = 0

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    max_gold = [0]
                    visited = [[0 for i in range(n)] for j in range(m)]
                    self.dfs(0, max_gold, grid, visited, i, j)
                    # print(\"i j cur_max: \", i, j, max_gold[0])
                    res = max(res, max_gold[0])
        return res
