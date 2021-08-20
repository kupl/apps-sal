class Solution:

    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        for i in range(n - 2, -1, -1):
            mn = min(A[i + 1])
            idx = A[i + 1].index(mn)
            for j in range(n):
                if j != idx:
                    A[i][j] += mn
                elif j == idx:
                    dp = [101 for _ in range(n)]
                    for k in range(n):
                        if k != idx:
                            dp[k] = A[i + 1][k]
                    A[i][j] += min(dp)
        return min(A[0])
