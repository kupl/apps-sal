class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.maxX = len(grid[0]) - 1
        self.maxY = len(grid) - 1
        self.maxGold = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                if grid[y][x] != 0:
                    self.helper(x, y, grid, 0)
        return self.maxGold

    def helper(self, x, y, grid, gold):
        gold += grid[y][x]
        left = 0 if x - 1 < 0 else grid[y][x - 1]
        right = 0 if x + 1 > self.maxX else grid[y][x + 1]
        top = 0 if y - 1 < 0 else grid[y - 1][x]
        bottom = 0 if y + 1 > self.maxY else grid[y + 1][x]
        if left == 0 and right == 0 and (top == 0) and (bottom == 0):
            if gold > self.maxGold:
                self.maxGold = gold
            return
        tmp = grid[y][x]
        grid[y][x] = 0
        if left != 0:
            self.helper(x - 1, y, grid, gold)
        if right != 0:
            self.helper(x + 1, y, grid, gold)
        if top != 0:
            self.helper(x, y - 1, grid, gold)
        if bottom != 0:
            self.helper(x, y + 1, grid, gold)
        grid[y][x] = tmp
