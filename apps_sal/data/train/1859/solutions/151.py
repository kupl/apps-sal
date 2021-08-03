class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        '''
        f[i][j] = 以(i,j)为右下角的最大square边长
        '''
        row, col = len(matrix), len(matrix[0])
        f = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    f[i][j] = 0
                    continue
                if i == 0 or j == 0:
                    f[i][j] = matrix[i][j]
                    continue

                f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1

        return sum([sum(f[i]) for i in range(row)])
