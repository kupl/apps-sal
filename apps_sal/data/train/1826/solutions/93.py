class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        f = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    for i_ in range(i, i + K + 1):
                        for j_ in range(j, j + K + 1):
                            if i_ < m and j_ < n:
                                f[i][j] += mat[i_][j_]
                elif j == 0:
                    f[i][j] = f[i - 1][j]
                    if i - 1 - K >= 0:
                        for j_ in range(j, j + K + 1):
                            if j_ < n:
                                f[i][j] -= mat[i - 1 - K][j_]
                                
                    if i + K < m:
                        for j_ in range(j, j + K + 1):
                            if j_ < n:
                                f[i][j] += mat[i + K][j_]
                else:
                    f[i][j] = f[i][j - 1]
                    if j - 1 - K >= 0:
                        for i_ in range(i - K, i + K + 1):
                            if 0 <= i_ < m:
                                f[i][j] -= mat[i_][j - 1 - K]
                                
                    if j + K < n:
                        for i_ in range(i - K, i + K + 1):
                            if 0 <= i_ < m:
                                f[i][j] += mat[i_][j + K]
        return f
