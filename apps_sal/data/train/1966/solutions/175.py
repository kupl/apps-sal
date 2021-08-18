class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        count = 0
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            c = 0
            for j in range(m - 1, -1, -1):
                if mat[i][j]:
                    c += 1
                else:
                    c = 0
                dp[i][j] = c
        for j in range(m):
            for i in range(n):
                if dp[i][j]:
                    min_v = dp[i][j]
                    count += dp[i][j]
                    for k in range(i + 1, n):
                        min_v = min(min_v, dp[k][j])
                        if not min_v:
                            break
                        count += (k - i + 1) * min_v - (k - i) * min_v
        return count
