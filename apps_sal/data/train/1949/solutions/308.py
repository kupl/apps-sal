class Solution:
    def __init__(self):
        self.max_gold = float('-Inf')

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def dfs(current, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return
            current += grid[i][j]
            temp = grid[i][j]
            grid[i][j] = 0
            self.max_gold = max(current, self.max_gold)

            dfs(current, i - 1, j)
            dfs(current, i + 1, j)
            dfs(current, i, j - 1)
            dfs(current, i, j + 1)
            grid[i][j] = temp

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    dfs(0, i, j)
        return self.max_gold if self.max_gold != float('-Inf') else 0
