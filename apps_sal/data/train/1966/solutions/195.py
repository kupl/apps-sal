class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        if m == 0: return 0
        n = len(mat[0])
        if n == 0: return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[i][j] = mat[i][j]
                else:
                    if mat[i][j] == 1:
                        dp[i][j] = dp[i][j-1] + 1
        result = 0
        for i in range(m):
            for j in range(n):
                min_width = dp[i][j]
                for row_idx in range(i,-1,-1):
                    min_width = min(min_width, dp[row_idx][j])
                    result += min_width
                    if min_width == 0:
                        break
        return result

