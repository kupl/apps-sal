class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])

        dp = [[None] * col for _ in range(row)]

        for i in range(row):
            count = 0
            for j in range(col):
                if mat[i][j] == 1:
                    count += 1
                else:
                    count = 0
                dp[i][j] = count

        res = 0
        for i in range(row):
            for j in range(col):
                mn = float('inf')
                for k in range(i, row):
                    mn = min(mn, dp[k][j])
                    res += mn
        return res
