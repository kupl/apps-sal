class Solution:
    def getMaximumGold(self, grid: [[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Search max possible return starting from this cell
                result = max(self.search(grid, i, j), result)
        return result

    def search(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 0
        if grid[x][y] == 0:
            return 0

        result = grid[x][y]
        temp = result
        # Mark as 0 to show gold has been taken
        grid[x][y] = 0

        # Search all neighbours
        result += max(self.search(grid, x - 1, y),
                      self.search(grid, x, y - 1),
                      self.search(grid, x + 1, y),
                      self.search(grid, x, y + 1))

        # Restore original gold in this cell for another path.  This is
        # because grid is passed as reference, so one modifying it during one
        # path will affect another (even though it may not have visited yet)
        grid[x][y] = temp

        return result
