class Solution:
    # iterate over every square and then fan out to n x n matrices and increment if all 1
    def countSquares(self, matrix: List[List[int]]) -> int:
        ret = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    sublen = 1
                    check = 1
                    while check == 1 and row + sublen <= len(matrix) and col + sublen <= len(matrix[0]):
                        for ncol in range(col, col + sublen):
                            if matrix[row + sublen - 1][ncol] == 0:
                                check = 0
                                break
                        for nrow in range(row, row + sublen):
                            if matrix[nrow][col + sublen - 1] == 0:
                                check = 0
                                break
                        sublen += 1
                        ret += check
        return ret
