class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold = 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] > 0:
                    max_gold = max(max_gold, self.get_gold(grid, row, col))
        return max_gold

    def get_gold(self, grid, row, col):
        if (row < 0 or row >= len(grid)
          or col < 0 or col >= len(grid[row])
          or grid[row][col] == 0):
            return 0

        ori = grid[row][col]
        gold = 0
        grid[row][col] = 0

        gold = max(gold, self.get_gold(grid, row + 1, col))
        gold = max(gold, self.get_gold(grid, row - 1, col))
        gold = max(gold, self.get_gold(grid, row, col + 1))
        gold = max(gold, self.get_gold(grid, row, col - 1))

        grid[row][col] = ori

        return gold + ori

