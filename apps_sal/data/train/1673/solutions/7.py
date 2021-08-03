class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        A = arr
        n = len(A)
        for i in range(1, n):
            for j in range(n):
                res = A[i - 1][0:j] + A[i - 1][j + 1:n]
                A[i][j] += min(res)
        return min(A[n - 1])
