import itertools as it


class Solution:

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        nrows = len(grid)
        ncols = len(grid[0])
        cum_rows = [list(it.accumulate(grid[row], initial=0)) for row in range(nrows)]
        cum_cols = [list(it.accumulate((grid[row][col] for row in range(nrows)), initial=0)) for col in range(ncols)]
        ans = 0
        for (row1, col1) in it.product(range(nrows), range(ncols)):
            if grid[row1][col1] == 0:
                continue
            side = 0
            while row1 + side < nrows and col1 + side < ncols:
                row2 = row1 + side
                col2 = col1 + side
                if cum_cols[col1][row2 + 1] - cum_cols[col1][row1] == side + 1 and cum_cols[col2][row2 + 1] - cum_cols[col2][row1] == side + 1 and (cum_rows[row1][col2 + 1] - cum_rows[row1][col1] == side + 1) and (cum_rows[row2][col2 + 1] - cum_rows[row2][col1] == side + 1):
                    ans = max(ans, (side + 1) ** 2)
                side += 1
        return ans
