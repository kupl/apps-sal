class Solution:

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        result = True
        for i in range(len(matrix) - 1):
            result = result and matrix[i][:-1] == matrix[i + 1][1:]
        return result
