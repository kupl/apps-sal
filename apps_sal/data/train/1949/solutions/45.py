class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    max_gold = max(max_gold, self.searchGrid(grid, i, j, 0))

        return max_gold

    def searchGrid(self, grid, i, j, gold):

        square_gold = grid[i][j]
        gold += square_gold
        grid[i][j] = 0

        up_gold = left_gold = down_gold = right_gold = gold
        if i > 0 and grid[i - 1][j]:
            up_gold = self.searchGrid(grid, i - 1, j, gold)

        if j > 0 and grid[i][j - 1]:
            left_gold = self.searchGrid(grid, i, j - 1, gold)

        if i < len(grid) - 1 and grid[i + 1][j]:
            down_gold = self.searchGrid(grid, i + 1, j, gold)

        if j < len(grid[0]) - 1 and grid[i][j + 1]:
            right_gold = self.searchGrid(grid, i, j + 1, gold)

        grid[i][j] = square_gold

        return max(up_gold, left_gold, down_gold, right_gold)
