class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        RangeSum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                RangeSum[i][j] = RangeSum[i - 1][j] + RangeSum[i][j - 1] - RangeSum[i - 1][j - 1] + mat[i - 1][j - 1]

        ans = [[0 for _ in range(n)] for _ in range(m)]

        print(RangeSum)

        for r in range(m):
            for c in range(n):
                i2 = min(m - 1, r + K)
                j2 = min(n - 1, c + K)
                i1 = max(0, r - K)
                j1 = max(0, c - K)
                ans[r][c] = RangeSum[i2 + 1][j2 + 1] - RangeSum[i2 + 1][j1] - RangeSum[i1][j2 + 1] + RangeSum[i1][j1]

        return ans
