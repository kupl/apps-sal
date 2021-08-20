class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        ret = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    sublen = 1
                    while row + sublen <= len(matrix) and col + sublen <= len(matrix[0]) and (0 not in [matrix[row + sublen - 1][ncol] for ncol in range(col, col + sublen)]) and (0 not in [matrix[nrow][col + sublen - 1] for nrow in range(row, row + sublen)]):
                        ret += 1
                        sublen += 1
        return ret
