class Solution:

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        (x, y) = (len(matrix[0]), len(matrix))
        for i in range(x - 1):
            for j in range(y - 1):
                if matrix[j][i] != matrix[j + 1][i + 1]:
                    return False
        return True
