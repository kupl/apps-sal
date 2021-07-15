class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        res = []
        for i in range(K + 1):
            res.append([0] * (n + 2 * (K + 1)))
        for i in range(m):
            res.append([0] * (K + 1) + mat[i] + [0] * (K + 1))
        for i in range(K + 1):
            res.append([0] * (n + 2 * (K + 1)))
        
        for i in range(1, m + 2*(K + 1)):
            for j in range(1, n + 2*(K + 1)):
                res[i][j] = res[i][j] + res[i - 1][j] + res[i][j - 1] - res[i - 1][j - 1]

        for i in range(K + 1, m + K + 1):
            for j in range(K + 1, n + K + 1):
                mat[i - K - 1][j - K - 1] = res[i + K][j + K] - (res[i + K][j - K - 1] + res[i - K - 1][j + K] - res[i - K - 1][j - K - 1])
        return mat
        

