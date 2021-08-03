class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        dp = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0]) - 1, -1, -1):
                if mat[i][j] == 1:
                    dp[i][j] = 1 + (dp[i][j + 1] if j < len(mat[0]) - 1 else 0)

        ans = 0
        for j in range(len(mat[0])):
            for i in range(len(mat)):
                t = float('inf')

                for k in range(i, len(mat)):
                    t = min(t, dp[k][j])

                    if t == 0:
                        break
                    else:
                        ans += t

        return ans
