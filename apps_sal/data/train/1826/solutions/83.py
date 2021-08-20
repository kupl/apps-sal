import copy


class Solution:

    def matrixBlockSum(self, G: List[List[int]], K: int) -> List[List[int]]:
        (M, N, G[0]) = (len(G), len(G[0]), list(itertools.accumulate(G[0])))
        A = [[0] * N for _ in range(M)]
        for i in range(1, M):
            s = 0
            for j in range(N):
                s += G[i][j]
                G[i][j] = s + G[i - 1][j]
        for (i, j) in itertools.product(list(range(M)), list(range(N))):
            (R, C) = (min(M - 1, i + K), min(N - 1, j + K))
            A[i][j] = G[R][C] - (i - K > 0 and G[i - K - 1][C]) - (j - K > 0 and G[R][j - K - 1]) + (i - K > 0 and j - K > 0 and G[i - K - 1][j - K - 1])
        return A
