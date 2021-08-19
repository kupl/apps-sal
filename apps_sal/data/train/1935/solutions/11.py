class Solution:

    def isToeplitzMatrix1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        (row, col) = (len(matrix), len(matrix[0]))
        for j in range(col):
            a = 0
            while a + 1 < row and j + a + 1 < col:
                if matrix[a][j + a] == matrix[a + 1][j + a + 1]:
                    a += 1
                else:
                    return False
        for i in range(row):
            a = 0
            while a + 1 < col and i + 1 + a < row:
                if matrix[i + a][a] == matrix[i + a + 1][a + 1]:
                    a += 1
                else:
                    return False
        return True

    def isToeplitzMatrix(self, m):
        return all((m[i][j] == m[i + 1][j + 1] for i in range(len(m) - 1) for j in range(len(m[0]) - 1)))
