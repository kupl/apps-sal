class Solution:
    def numSubmat(self, g: List[List[int]]) -> int:
        # traverse grid, if value is \"1\"
        # record increasing \"width\" from left, or clear to zero on grid == 0
        # across rows, submatrix count is:
        # current width + min(curr width, prev width) + ...
        # stepping down till grid boundary or g[r][c] zero value
        # O(MN * N) time, O(1) space

        rows, cols, res = len(g), len(g[0]), 0

        for r in range(rows):
            width = 0
            for c in range(cols):
                # increment row width from left
                if g[r][c]:
                    width += 1
                    g[r][c] = width
                else:
                    width = 0

                # account for current row submatrix count
                res += width

                # account for previous row submatrix count
                row, prev_width = r, width
                while row > 0 and g[row - 1][c]:
                    prev_width = min(prev_width, g[row - 1][c])
                    res = res + prev_width
                    row -= 1

        return res
