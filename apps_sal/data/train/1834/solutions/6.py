class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n, ans = len(A), len(A[0]), 0
        for c in range(n):
            col = sum(A[r][c] == A[r][0] for r in range(m))
            ans += max(col, m - col) * 2 ** (n - 1 - c)
        return ans
