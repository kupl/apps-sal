class Solution:

    def maxEqualRowsAfterFlips(self, mat: List[List[int]]) -> int:
        ans = 0
        (m, n) = (len(mat), len(mat[0]))
        ones = [[0] * n for i in range(m)]
        zeros = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    zeros[i][j] = 1
                else:
                    ones[i][j] = 1
        for i in range(m):
            for target in [ones[i], zeros[i]]:
                count = 1
                for k in range(m):
                    if k == i:
                        continue
                    if ones[k] == target or zeros[k] == target:
                        count += 1
                ans = max(ans, count)
        return ans
