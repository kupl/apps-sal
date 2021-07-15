import numpy as np
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        padded = np.pad(np.asarray(mat), K)
        result = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                result[i][j] = np.sum(padded[i:i + 2 * K + 1, j:j + 2 * K + 1])
        return result
