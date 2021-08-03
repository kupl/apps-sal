class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix == []:
            return 0
        maxval = 0
        for i in range(len(matrix[0])):
            if matrix[0][i] == 1:
                maxval += 1

        for i in range(1, len(matrix)):
            if matrix[i][0] == 1:
                maxval += 1
        print(maxval)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]:

                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                    maxval += matrix[i][j]
        for j in matrix:
            print((*j))
        return maxval
