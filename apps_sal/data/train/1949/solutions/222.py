class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        return max([self.helper(grid, row, col) for row in range(len(grid)) for col in range(len(grid[row]))])

    def helper(self, grid, row, col):
        if not self.are_valid_coordinates(grid, row, col):
            return 0
        curr_gold = grid[row][col]
        grid[row][col] = -1
        all_results = [curr_gold] + [curr_gold + self.helper(grid, nrow, ncol) for (nrow, ncol) in self.get_neighbors(row, col)]
        grid[row][col] = curr_gold
        return max(all_results)

    def are_valid_coordinates(self, grid, row, col):
        return row >= 0 and col >= 0 and (row < len(grid)) and (col < len(grid[row])) and (grid[row][col] > 0)

    def get_neighbors(self, row, col):
        return [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
