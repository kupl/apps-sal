class Solution:
    def numSubmat(self, mat) -> int:
        m, n = len(mat), len(mat[0])
        self.count = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    if j > 0:
                        mat[i][j] += mat[i][j - 1]

        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    row = i
                    submatrix_width = mat[i][j]
                    while row < m and mat[row][j]:
                        submatrix_width = min(submatrix_width, mat[row][j])
                        self.count += submatrix_width
                        row += 1
        return self.count
