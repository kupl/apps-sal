class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res = 0

        def dfs(x, y, grid):
            if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1 or grid[x][y] == 0:
                return 0
            temp = grid[x][y]
            grid[x][y] = 0
            a = dfs(x + 1, y, grid) + temp

            b = dfs(x, y + 1, grid) + temp
            c = dfs(x - 1, y, grid) + temp
            d = dfs(x, y - 1, grid) + temp
            res = max([a, b, c, d])
            grid[x][y] = temp
            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    res = max(dfs(i, j, grid), res)
        return (res)
