class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        M = len(mat)
        N = len(mat[0])

        if (K) >= (M - 1) and (K) >= (N - 1):
            t = 0
            for h in mat:
                for w in h:
                    t += w
            rtv = [[t] * N for _ in range(M)]
            return rtv

        def calc(presums, h, w, K):
            h1 = h - K
            h2 = h + K + 1
            w1 = w - K
            w2 = w + K + 1

            w1 = max(w1, 0)
            h1 = max(h1, 0)
            w2 = min(w2, N)
            h2 = min(h2, M)

            return presums[h1][w1] + presums[h2][w2] - presums[h1][w2] - presums[h2][w1]

        presums = [[0] * (N + 1) for _ in range(M + 1)]

        for h in range(M):
            for w in range(N):
                presums[h + 1][w + 1] = presums[h + 1][w] + presums[h][w + 1] - presums[h][w] + mat[h][w]

        rtv = [[0] * (N) for _ in range(M)]

        for h in range(M):
            for w in range(N):
                rtv[h][w] = calc(presums, h, w, K)

        return rtv
