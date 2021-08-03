class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        ans = (1 << N - 1) * M
        for j in range(1, N):
            count = sum(A[i][j] == A[i][0] for i in range(M))
            ans += max(count, M - count) << N - j - 1
        return ans
