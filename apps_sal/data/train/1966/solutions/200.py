def no_of_submat(r, c):
    return r * c


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
                    count += no_of_submat(1, dp[i][j])
                    for k in range(i + 1, n):
                        min_v = min(min_v, dp[k][j])
                        if not min_v:
                            break
                        count += no_of_submat(k - i + 1, min_v) - no_of_submat(k - i, min_v)
        return count
