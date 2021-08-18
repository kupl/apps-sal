class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        if not mat:
            self.cum_matrix = [[]]
        else:
            nrow = len(mat)
            ncol = len(mat[0])

            self.cum_matrix = [[0] * ncol for _ in range(nrow)]

            self.cum_matrix[0][0] = mat[0][0]
            for i in range(1, ncol):
                self.cum_matrix[0][i] = self.cum_matrix[0][i - 1] + mat[0][i]
            for j in range(1, nrow):
                self.cum_matrix[j][0] = self.cum_matrix[j - 1][0] + mat[j][0]

            for c in range(1, ncol):
                for r in range(1, nrow):
                    self.cum_matrix[r][c] = (self.cum_matrix[r - 1][c] + self.cum_matrix[r][c - 1] -
                                             self.cum_matrix[r - 1][c - 1] + mat[r][c])

        res = [[0] * ncol for _ in range(nrow)]

        if not self.cum_matrix:
            return []

        for r in range(nrow):
            for c in range(ncol):
                row1 = max(0, r - K)
                col1 = max(0, c - K)
                row2 = min(nrow - 1, r + K)
                col2 = min(ncol - 1, c + K)

                if row1 == 0 and col1 == 0:
                    res[r][c] = (self.cum_matrix[row2][col2])
                elif row1 == 0 and col1 > 0:
                    res[r][c] = (self.cum_matrix[row2][col2] -
                                 self.cum_matrix[row2][col1 - 1])
                elif row1 > 0 and col1 == 0:
                    res[r][c] = (self.cum_matrix[row2][col2] -
                                 self.cum_matrix[row1 - 1][col2])
                else:
                    res[r][c] = (self.cum_matrix[row2][col2] - self.cum_matrix[row1 - 1][col2] -
                                 self.cum_matrix[row2][col1 - 1] + self.cum_matrix[row1 - 1][col1 - 1])

        return res
