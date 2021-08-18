def is_valid_cell(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_amount = 0

        def backtrack(row, col, rows, cols, grid):
            if not is_valid_cell(row, col, rows, cols) or grid[row][col] == 0:
                return 0

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            original = grid[row][col]
            grid[row][col] = 0

            max_sum = 0
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                max_sum = max(max_sum, backtrack(r, c, rows, cols, grid))

            grid[row][col] = original

            return original + max_sum

        for row in range(rows):
            for col in range(cols):
                ans = backtrack(row, col, rows, cols, grid)
                max_amount = max(max_amount, ans)

        return max_amount
