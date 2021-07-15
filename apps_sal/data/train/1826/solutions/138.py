import numpy as np
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        padded = np.pad(np.asarray(mat), K)
        # conv = np.ones(2 * K + 1, 2 * K + 1)
        result = [[0] * m for _ in range(n)]
        # print(padded)
        for i in range(n):
            for j in range(m):
                result[i][j] = np.sum(padded[i:i + 2 * K + 1, j:j + 2 * K + 1])
                # for row in padded[i:i + 2 * K + 1, j:j + 2 * K + 1]:
                    # print(i,j, row, 2 * K)
                # print()
        return result
