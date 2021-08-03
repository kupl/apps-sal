class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 0:
                temp = grid[i][j]
                grid[i][j] = 0
                d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                summax = 0
                for m, n in d:
                    x = i + m
                    y = j + n
                    summax = max(summax, dfs(grid, x, y))
                grid[i][j] = temp
                return temp + summax
            else:
                return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, dfs(grid, i, j))
        return res
