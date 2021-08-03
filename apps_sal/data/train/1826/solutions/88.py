class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        cum_sum = [[0 for x in range(n + 1)] for y in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 0 and j == 0:
                    cum_sum[i][j] = mat[i - 1][j - 1]
                elif i == 0:
                    cum_sum[i][j] = mat[i - 1][j - 1] + cum_sum[i][j - 1]
                elif j == 0:
                    cum_sum[i][j] = mat[i - 1][j - 1] + cum_sum[i - 1][j]
                else:
                    cum_sum[i][j] = mat[i - 1][j - 1] + cum_sum[i - 1][j] + cum_sum[i][j - 1] - cum_sum[i - 1][j - 1]
        ans = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                maxr = min(i + K, m - 1) + 1
                maxc = min(j + K, n - 1) + 1
                minr = max(i - K - 1, -1) + 1
                minc = max(j - K - 1, -1) + 1
                ans[i][j] = cum_sum[maxr][maxc] - cum_sum[maxr][minc] - cum_sum[minr][maxc] + cum_sum[minr][minc]
        return ans
