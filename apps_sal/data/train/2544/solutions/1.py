class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:

        max_rows = [0 for _ in grid]
        max_cols = [0 for _ in grid]

        total_nonzero = 0

        for r in range(len(grid)):

            for c in range(len(grid[r])):

                if grid[r][c] > max_cols[c]:
                    max_cols[c] = grid[r][c]

                if grid[r][c] > max_rows[r]:
                    max_rows[r] = grid[r][c]

                if grid[r][c] > 0:
                    total_nonzero += 1

        print(max_rows)
        print(max_cols)
        print(total_nonzero)

        return sum(max_rows) + sum(max_cols) + total_nonzero
