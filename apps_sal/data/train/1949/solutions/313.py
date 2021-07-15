class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, gold):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
                return gold
            temp = grid[i][j]
            grid[i][j] = 0
            res = max(
                dfs(i - 1, j, gold + temp),
                dfs(i + 1, j, gold + temp),
                dfs(i, j - 1, gold + temp),
                dfs(i, j + 1, gold + temp)
            )
            grid[i][j] = temp
            return res
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    res = max(res, dfs(i, j, 0))
        return res
