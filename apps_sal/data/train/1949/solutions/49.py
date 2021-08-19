class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result = max(self.search(grid, i, j, set()), result)
        return result

    def search(self, grid, x, y, visited):
        if x < 0 or x >= len(grid) or y < 0 or (y >= len(grid[0])):
            return 0
        if grid[x][y] == 0:
            return 0
        if (x, y) in visited:
            return 0
        result = grid[x][y]
        visited.add((x, y))
        result += max(self.search(grid, x - 1, y, visited), self.search(grid, x, y - 1, visited), self.search(grid, x + 1, y, visited), self.search(grid, x, y + 1, visited))
        visited.remove((x, y))
        return result
