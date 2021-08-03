class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def findMaxGold(grid, i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] > 0:
                origin = grid[i][j]
                grid[i][j] = 0
                d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
                maxGold = 0
                for d1, d2 in d:
                    maxGold = max(maxGold, findMaxGold(grid, i + d1, j + d2))
                grid[i][j] = origin
                return origin + maxGold
            else:
                return 0

        maxGold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxGold = max(maxGold, findMaxGold(grid, i, j))
        return maxGold
