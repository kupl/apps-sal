class Solution:

    def matrixScore(self, A: List[List[int]]) -> int:
        (N, M) = (len(A), len(A[0]))
        res = 0
        for jj in range(M):
            num = 0
            for ii in range(N):
                num += A[ii][jj] ^ A[ii][0]
            res += max(num, N - num) * 2 ** (M - jj - 1)
        return res
