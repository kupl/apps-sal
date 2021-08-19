from typing import List


class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        num_islands = 0
        for (row_index, row) in enumerate(grid):
            for (col_index, val) in enumerate(row):
                if val == 0 and self.check_island(grid, row_index, col_index):
                    num_islands += 1
        return num_islands

    def check_island(self, grid: List[List[int]], row: int, col: int) -> bool:
        if row < 0 or row >= len(grid) or col < 0 or (col >= len(grid[0])):
            return False
        if grid[row][col] == 1:
            return True
        grid[row][col] = 1
        top = self.check_island(grid, row - 1, col)
        bottom = self.check_island(grid, row + 1, col)
        right = self.check_island(grid, row, col + 1)
        left = self.check_island(grid, row, col - 1)
        return top and bottom and right and left
