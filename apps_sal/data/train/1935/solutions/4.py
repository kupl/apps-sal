class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for c in range(len(matrix) - 1):
            for r in range(len(matrix[0]) - 1):
                if (matrix[c][r] != matrix[c + 1][r + 1]):
                    return False
        return True
