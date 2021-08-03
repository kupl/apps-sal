class Solution:
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        dp = [[None for i in range(n)] for j in range(m)]

        for i in range(m):
            count = 0

            for j in range(n - 1, -1, -1):
                if mat[i][j]:
                    count += 1
                else:
                    count = 0
                dp[i][j] = count

        res = 0
        for i in range(m):
            for j in range(n):
                min_val = float('inf')

                for k in range(i, m):
                    min_val = min(min_val, dp[k][j])
                    res += min_val

        return res
