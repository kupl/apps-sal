class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        result = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    for r in range(max(i - K, 0), min(i + K + 1, n)):
                        for c in range(max(j - K, 0), min(j + K + 1, m)):
                            result[i][j] += mat[r][c]
                elif j > 0:
                    prev_c = j - 1
                    result[i][j] += result[i][prev_c]
                    for r in range(max(i - K, 0), min(i + K + 1, n)):
                        if j - K - 1 >= 0:
                            result[i][j] -= mat[r][j - K - 1]
                        if j + K < m:
                            result[i][j] += mat[r][j + K]
                else:
                    prev_r = i - 1
                    result[i][j] += result[prev_r][j]
                    for c in range(max(j - K, 0), min(j + K + 1, m)):
                        if i - K - 1 >= 0:
                            result[i][j] -= mat[i - K - 1][c]
                        if i + K < n:
                            result[i][j] += mat[i + K][c]
        return result
