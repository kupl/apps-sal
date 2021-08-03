class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        # Obvious DP for O(MNK), do a second DP to bring down to O(MN)
        M, N = len(mat), len(mat[0])
        tsum, lsum = [[0 for _ in range(N)] for _ in range(M)], [[0 for _ in range(N)] for _ in range(M)]
        for i in range(M):
            for j in range(N):
                tsum[i][j] = (0 if i == 0 else tsum[i - 1][j]) + mat[i][j]
                lsum[i][j] = (0 if j == 0 else lsum[i][j - 1]) + mat[i][j]

        ans = [[0 for _ in range(N)] for _ in range(M)]

        def l(i, j):
            if j >= N:
                return l(i, N - 1)
            elif 0 <= i < M and 0 <= j < N:
                return lsum[i][j]
            return 0

        def t(i, j):
            if i >= M:
                return t(M - 1, j)
            elif 0 <= i < M and 0 <= j < N:
                return tsum[i][j]
            return 0

        for i in range(min(M, K + 1)):
            for j in range(min(N, K + 1)):
                ans[0][0] += mat[i][j]
        for i in range(1, M):
            ans[i][0] = ans[i - 1][0] + l(i + K, K) - l(i - K - 1, K)
        for j in range(1, N):
            ans[0][j] = ans[0][j - 1] + t(K, j + K) - t(K, j - K - 1)
        for i in range(1, M):
            for j in range(1, N):
                tl = ans[i - 1][j - 1]
                add = l(i + K, j + K) - l(i + K, j - K - 1) + t(i + K - 1, j + K) - t(i - K - 1, j + K)
                sub = t(i + K - 1, j - K - 1) - t(i - K - 2, j - K - 1) + l(i - K - 1, j + K - 1) - l(i - K - 1, j - K - 1)
                ans[i][j] = tl + add - sub
        return ans
