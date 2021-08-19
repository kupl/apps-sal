class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def search(x, y):
            if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] == 0:
                return 0
            origin = grid[x][y]
            grid[x][y] = 0  # mark as visited

            maxGold = 0

            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                maxGold = max(maxGold, search(nx, ny))

            grid[x][y] = origin

            return maxGold + origin

        return max(search(i, j) for i in range(len(grid)) for j in range(len(grid[0])))
