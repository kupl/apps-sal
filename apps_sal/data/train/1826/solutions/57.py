class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dp = []
        for i in range(m + 2 * K):
            row = []
            for j in range(n + 2 * K):
                row.append(0)
            dp.append(row)

        for i in range(m):
            for j in range(n):
                dp[K + i][K + j] = mat[i][j]

        for i in range(m):

            for j in range(n):
                temp = 0
                for i1 in range(-K, K + 1):
                    temp += sum(dp[i1 + K + i][j:j + 2 * K + 1])

                mat[i][j] = temp
        return mat
