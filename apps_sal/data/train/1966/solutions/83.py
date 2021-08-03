class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # get potential widths of rectangles, then process downward for all rectangles defined by width

        # process widths
        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            for c in range(1, cols):
                mat[r][c] = 1 + mat[r][c - 1] if mat[r][c] else 0

        # process downwards for each potential width
        rectangles = 0
        for r in range(rows):
            for c in range(cols):
                width = mat[r][c]
                if width:
                    row = r
                    while row < rows:
                        width = min(width, mat[row][c])
                        rectangles += width
                        row += 1

        return rectangles
