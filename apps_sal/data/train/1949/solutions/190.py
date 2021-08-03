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
        if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
            return False

        if (grid[x][y] == 0 or (x, y) in visited):
            return False
        return True

    def recursive(self, total, x, y, grid, visited, checked):
        visited = set(visited)
        visited.add((x, y))
        total = total + grid[x][y]

        vTop = False
        vBtm = False
        vRight = False
        vLeft = False

        left, right, top, btm = 0, 0, 0, 0

        if (self.valid(x - 1, y, grid, visited)):
            # print('top')
            top = self.recursive(total, x - 1, y, grid, visited, checked)
            vTop = self.valid(x - 1, y, grid, visited)

        if (self.valid(x + 1, y, grid, visited)):
            # print('btm')
            btm = self.recursive(total, x + 1, y, grid, visited, checked)
            vBtm = self.valid(x + 1, y, grid, visited)

        if (self.valid(x, y - 1, grid, visited)):
            # print('left')
            left = self.recursive(total, x, y - 1, grid, visited, checked)
            vLeft = self.valid(x, y - 1, grid, visited)

        if (self.valid(x, y + 1, grid, visited)):
            # print('right')
            right = self.recursive(total, x, y + 1, grid, visited, checked)
            vRight = self.valid(x, y + 1, grid, visited)

        gotPath = vLeft or vRight or vTop or vBtm
        # if (gotPath):
        #     checked.add((x,y))

        return max(left, right, top, btm, total)
