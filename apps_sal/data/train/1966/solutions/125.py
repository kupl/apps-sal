class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        if not m:
            return 0
        n = len(mat[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j - 1] + 1
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                row = i
                minWidth = math.inf
                while row >= 0 and mat[i][j]:
                    minWidth = min(minWidth, dp[row][j])
                    res += minWidth
                    row -= 1
        return res
