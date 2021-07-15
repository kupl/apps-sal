class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m = len(arr)
        n = len(arr[0])
        dp = [[0]*n for i in range(m)]

        for j in range(n):
            dp[0][j] = arr[0][j]

        for i in range(1,m):
            sorted_lastrow = sorted([(k, dp[i - 1][k]) for k in range(n)], key=lambda x: x[1])
            p_index, p = sorted_lastrow[0]
            q_index, q = sorted_lastrow[1]
            
            for j in range(n):

                

                lastdp = p if p_index != j else q
                dp[i][j] = lastdp + arr[i][j]

        return min(dp[m-1])

