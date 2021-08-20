class Solution:

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        hashMap = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if hashMap.get(i - j, 'no') != 'no':
                    if hashMap[i - j] != matrix[i][j]:
                        return False
                else:
                    hashMap[i - j] = matrix[i][j]
        return True
