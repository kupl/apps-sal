class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        ans = 0
        for i1 in range(m):
            dp = [0] * n
            for i2 in range(i1, m):
                for j in range(n):
                    dp[j] += mat[i2][j]

                l = 0
                j = 0
                while j < n:
                    if dp[j] == i2 - i1 + 1:
                        l += 1
                    else:
                        ans += l * (l + 1) // 2
                        l = 0

                    j += 1

                if l > 0:
                    ans += l * (l + 1) // 2

        return ans
