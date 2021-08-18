class Solution:
    def getMaximumGold(self, grid: [[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result = max(self.search(grid, i, j), result)
        return result

    def search(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 0
        if grid[x][y] == 0:
            return 0

        result = grid[x][y]
        temp = result
        grid[x][y] = 0

        result += max(self.search(grid, x - 1, y),
                      self.search(grid, x, y - 1),
                      self.search(grid, x + 1, y),
                      self.search(grid, x, y + 1))

        grid[x][y] = temp

        return result
