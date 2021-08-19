class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = [[mat[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n - 2, -1, -1):
                if mat[i][j] == 1:
                    dp[i][j] = dp[i][j + 1] + 1
        res = 0
        for i in range(m):
            for j in range(n):
                k = i
                mn = dp[i][j]
                while k < m and dp[k][j] != 0:
                    mn = min(mn, dp[k][j])
                    res += mn
                    k += 1
        return res
