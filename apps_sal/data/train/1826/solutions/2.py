class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        k = K
        range_sum = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                top_left = range_sum[i-1][j-1] if j-1 >= 0 and i-1 >= 0 else 0
                top = range_sum[i-1][j] if i-1 >=0 else 0
                left = range_sum[i][j-1] if j-1>=0 else 0
                range_sum[i][j] = top + left - top_left + mat[i][j]
        print(range_sum)
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                # right_buttom point
                col = min(m-1, j+k)
                row = min(n-1, i+k)
                print([row, col])
                dp[i][j] = (range_sum[row][col]
                           + (range_sum[i-k-1][j-k-1] if i-k-1>=0 and j-k-1>=0 else 0)
                           - (range_sum[row][j-k-1] if j-k-1>=0 else 0)
                           - (range_sum[i-k-1][col] if i-k-1>=0 else 0))
        return dp
