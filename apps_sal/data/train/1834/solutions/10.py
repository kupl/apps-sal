class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])

        f = [0] * m

        for i in range(m):
            if A[i][0] == 0:
                f[i] = 1

        ans = 2 ** (n - 1) * m

        for j in range(1, n):
            cnt = sum(f[i] ^ A[i][j] for i in range(m))
            cnt = max(cnt, m - cnt)

            ans += 2 ** (n - 1 - j) * cnt

        return ans
