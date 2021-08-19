class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        (m, n) = (len(grid), len(grid[0]))

        def getMaxGoldForCoords(i, j):
            if i < 0 or i >= m or j < 0 or (j >= n):
                return 0
            if grid[i][j] == 0:
                return 0
            temp = grid[i][j]
            grid[i][j] = 0
            result = max(getMaxGoldForCoords(i + 1, j), getMaxGoldForCoords(i - 1, j), getMaxGoldForCoords(i, j + 1), getMaxGoldForCoords(i, j - 1)) + temp
            grid[i][j] = temp
            return result
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, getMaxGoldForCoords(i, j))
        return res
