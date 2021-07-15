from copy import deepcopy

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        matrix = deepcopy(mat)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                top = max(0, i - K)
                bottom = min(len(mat), i + K + 1)
                left = max(0, j - K)
                right = min(len(mat[0]), j + K + 1)
                matrix[i][j] = sum(map(sum, [row[left:right] for row in mat][top:bottom]))
        return matrix
