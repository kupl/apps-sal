class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]:
                    if c > 0:
                        mat[r][c] = mat[r][c - 1] + 1
        submatrices = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]:
                    row = r
                    min_value = mat[r][c]
                    while row < rows and mat[r][c]:
                        min_value = min(min_value, mat[row][c])
                        submatrices += min_value
                        row += 1
        return submatrices
