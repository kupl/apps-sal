class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.max_gold = 0
        self.row = len(grid)
        self.col = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.search_gold(grid, i, j, 0)

        return self.max_gold

    def search_gold(self, grid, i, j, val):
        pos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if i >= 0 and j >= 0 and i < self.row and j < self.col and grid[i][j]:
            temp = grid[i][j]
            val += grid[i][j]
            grid[i][j] = 0
            self.max_gold = max(self.max_gold, val)

            for x, y in pos:
                self.search_gold(grid, x + i, y + j, val)

            grid[i][j] = temp
