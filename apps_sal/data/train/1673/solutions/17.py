class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        A = arr
        n = len(A)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for c in range(n):
            dp[0][c] = A[0][c]
        
        for r in range(1, n):
            for c in range(n):
                prev = heapq.nsmallest(2, dp[r - 1])
                dp[r][c] = A[r][c]
                dp[r][c] += prev[1] if dp[r - 1][c] == prev[0] else prev[0]
        
        return min(dp[n - 1])
