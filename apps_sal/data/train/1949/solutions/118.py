class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        checked = set()
        maximum = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                # not 0
                if (grid[x][y] and (x, y) not in checked):
                    # print(\"checking: \" + str((x,y)))
                    visited = set()
                    value = self.recursive(0, x, y, grid, visited, checked)

                    if (value > maximum):
                        # print(\"new max point: \" + str((x,y)))
                        # print(\"new max: \" + str(value))
                        maximum = value
        return maximum

    # not zero and not visited
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
        # left = (x-1,y)
        # right = (x+1,y)
        # top = (x,y-1)
        # btm = (x,y+1)
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
