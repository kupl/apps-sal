class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        rval = []
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 0:
                    continue
                self.traverse(rval, grid, [grid[x][y]], {(x, y): True}, x, y)

        return max(rval or [0])

    def traverse(self, rval, grid, path, visited, x, y):
        if self.finished(grid, visited, x, y):
            rval.append(sum(path))
            return

        for new_x, new_y in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if not self.available(grid, visited, new_x, new_y):
                continue
            path.append(grid[new_x][new_y])
            visited[(x, y)] = True
            self.traverse(rval, grid, path, visited, new_x, new_y)
            path.pop(-1)
            visited[(x, y)] = False

    def available(self, grid, visited, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 0 and not visited.get((x, y), False)

    def finished(self, grid, visited, x, y):
        for new_x, new_y in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if self.available(grid, visited, new_x, new_y):
                return False
        return True
