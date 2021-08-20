class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or (j >= len(grid[0])) or (grid[i][j] == 0):
                return 0
            res = grid[i][j]
            grid[i][j] = 0
            cost = res + max(dfs(grid, i + 1, j), dfs(grid, i - 1, j), dfs(grid, i, j + 1), dfs(grid, i, j - 1))
            grid[i][j] = res
            return cost
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(grid, i, j))
        return max_gold
