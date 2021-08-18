class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        checked = set()
        maximum = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (grid[x][y] and (x, y) not in checked):
                    visited = set()
                    value = self.recursive(0, x, y, grid, visited, checked)

                    if (value > maximum):
                        maximum = value
        return maximum

    def valid(self, x, y, grid, visited):
        if (grid[x][y] == 0 or (x, y) in visited):
            return False
        return True

    def recursive(self, total, x, y, grid, visited, checked):
        if (not self.valid(x, y, grid, visited)):
            return total

        visited = set(visited)
        visited.add((x, y))
        total = total + grid[x][y]
        left, right, top, btm = total, total, total, total

        if (x > 0):
            left = self.recursive(total, x - 1, y, grid, visited, checked)

        if (x < len(grid) - 1):
            right = self.recursive(total, x + 1, y, grid, visited, checked)

        if (y > 0):
            top = self.recursive(total, x, y - 1, grid, visited, checked)

        if (y < len(grid[x]) - 1):
            btm = self.recursive(total, x, y + 1, grid, visited, checked)

        return max(left, right, top, btm, total)
