class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        (m, n) = (len(mat), len(mat[0]))
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            prev = 0
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 1:
                    dp[i][j] = prev + 1
                    prev = dp[i][j]
                else:
                    prev = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    min_right = dp[i][j]
                    for k in range(i, m):
                        min_right = min(min_right, dp[k][j])
                        res += min_right
        return res
