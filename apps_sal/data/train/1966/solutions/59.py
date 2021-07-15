class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        dp = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        res = 0
        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                if mat[i - 1][j - 1] == 1:
                    dp[i][j] = 1 + dp[i][j - 1]
                    res += dp[i][j]
                    
                    minRec = dp[i][j]
                    for k in range(i - 1, -1, -1):
                        minRec = min(minRec, dp[k][j])
                        res += minRec
        return res

