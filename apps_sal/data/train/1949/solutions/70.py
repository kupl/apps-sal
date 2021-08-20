class Solution:

    def explore(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or (col >= len(grid[0])) or (grid[row][col] == 0):
            return 0
        total = curr_gold = grid[row][col]
        max_gold = grid[row][col] = 0
        for (row_offset, col_offset) in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            max_gold = max(max_gold, self.explore(grid, row + row_offset, col + col_offset))
        grid[row][col] = curr_gold
        return total + max_gold

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_gold = max(max_gold, self.explore(grid, row, col))
        return max_gold
