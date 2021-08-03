class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        M, N = len(matrix), len(matrix[0])
        if M == 1:
            return True
        prev_row = matrix[0][:-1]
        for row in matrix[1:]:
            if row[1:] != prev_row:
                return False
            prev_row = row[:-1]
        return True
