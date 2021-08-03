class Solution:
    def matrixBlockSum(self, A: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(A), len(A[0])

        def force_inside(ra, rb, ca, cb):
            return max(0, ra), min(m, rb), max(0, ca), min(n, cb)

        def rect(i, j):
            return force_inside(i - K, i + K + 1, j - K, j + K + 1)

        def sum_rect(ra, rb, ca, cb):
            ra, rb, ca, cb = force_inside(ra, rb, ca, cb)
            s = 0
            for p in range(ra, rb):
                for q in range(ca, cb):
                    s += A[p][q]
            return s

        S = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                ra, rb, ca, cb = rect(i, j)
                if i == 0 and j == 0:
                    S[i][j] = sum_rect(ra, rb, ca, cb)
                else:
                    if j == 0:
                        i0, j0 = i - 1, 0
                    else:
                        i0, j0 = i, j - 1
                    ra0, rb0, ca0, cb0 = rect(i0, j0)
                    S[i][j] = S[i0][j0]
                    S[i][j] -= sum_rect(ra0, ra, ca, cb)
                    S[i][j] -= sum_rect(ra, rb, ca0, ca)
                    S[i][j] += sum_rect(rb0, rb, ca, cb)
                    S[i][j] += sum_rect(ra, rb, cb0, cb)
        return S
