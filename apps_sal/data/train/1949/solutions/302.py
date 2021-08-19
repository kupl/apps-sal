class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] <= 0:
                return 0

            val = grid[i][j]
            grid[i][j] = -1
            ret = val + max(dfs(grid, i - 1, j), dfs(grid, i + 1, j), dfs(grid, i, j - 1), dfs(grid, i, j + 1))
            grid[i][j] = val
            return ret

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Ideal of optimization: if the node should not be used as the start node,
                # do not do DFS on it. But this may be difficult to check.
                result = max(result, dfs(grid, i, j))

        return result
