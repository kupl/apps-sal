class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        dp = [[None for i in range(n)]for j in range(m)]

        for i in range(m):
            count = 0

            for j in range(n - 1, -1, -1):
                if mat[i][j]:
                    count += 1
                else:
                    count = 0
                dp[i][j] = count

        ans = 0

        for i in range(m):
            for j in range(n):

                mn = float('inf')
                for k in range(i, m):
                    mn = min(mn, dp[k][j])
                    ans += mn
                print()

        return ans
