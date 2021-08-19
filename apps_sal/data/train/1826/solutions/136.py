import numpy as np


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        # Edge case
        if not mat or not mat[0]:
            return []
        # General case
        mat = np.array(mat)
        m, n = mat.shape
        output = np.zeros((m, n), dtype=np.int)
        for i in range(m):
            for j in range(n):
                rowLB, rowUB = max(0, i - K), min(i + K, m - 1) + 1
                colLB, colUB = max(0, j - K), min(j + K, n - 1) + 1
                output[rowLB: rowUB, colLB: colUB] += mat[i][j] * np.ones((rowUB - rowLB, colUB - colLB), dtype=np.int)
        return output
