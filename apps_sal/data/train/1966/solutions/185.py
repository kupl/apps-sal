class Solution:
    def numSubmat(self, g: List[List[int]]) -> int:

        rows, cols, res = len(g), len(g[0]), 0

        for r in range(rows):
            width = 0
            for c in range(cols):
                if g[r][c]:
                    width += 1
                    g[r][c] = width
                else:
                    width = 0

                res += width

                row, prev_width = r, width
                while row > 0 and g[row - 1][c]:
                    prev_width = min(prev_width, g[row - 1][c])
                    res = res + prev_width
                    row -= 1

        return res
