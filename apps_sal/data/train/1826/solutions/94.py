import numpy as np
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        matrix= np.zeros((m+1, n+1))
        for i in range (m):
            for j in range (n):
                matrix[i+1][j+1]=matrix[i+1][j]+matrix[i][j+1]-matrix[i][j]+mat[i][j]
        result = np.zeros((m, n))
        for i in range(m):
            for j in range(n):
                x1=max(i-K, 0)
                y1=max(j-K, 0)
                x2=min(i+K+1, m)
                y2=min(j+K+1, n)
                result[i][j]=matrix[x2][y2]-matrix[x1][y2]-matrix[x2][y1]+matrix[x1][y1]
        return (result.astype(int))

