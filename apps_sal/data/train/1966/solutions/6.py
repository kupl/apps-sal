class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        m, n = len(mat), len(mat[0])

        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j - 1] + 1

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                row, minwidth = i, float('inf')
                while row >= 0 and mat[row][j]:
                    minwidth = min(minwidth, dp[row][j])
                    res += minwidth
                    row -= 1

        return res
