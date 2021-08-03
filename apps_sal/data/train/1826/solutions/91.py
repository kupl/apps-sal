class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        M = len(mat)
        if M == 0:
            return mat
        N = len(mat[0])

        for i in range(1, M):
            mat[i][0] += mat[i - 1][0]

        for j in range(1, N):
            mat[0][j] += mat[0][j - 1]

        for i in range(1, M):
            for j in range(1, N):
                mat[i][j] = (mat[i][j] + mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1])

        answer = [[0 for _ in range(N)] for _ in range(M)]

        for i in range(M):
            for j in range(N):
                rl = max(i - K, 0)
                cl = max(j - K, 0)
                rr = min(i + K, M - 1)
                cr = min(j + K, N - 1)

                A, B, C, D = 0, 0, 0, mat[rr][cr]

                if rl - 1 >= 0:
                    B = mat[rl - 1][cr]
                if cl - 1 >= 0:
                    C = mat[rr][cl - 1]
                if rl - 1 >= 0 and cl - 1 >= 0:
                    A = mat[rl - 1][cl - 1]

                answer[i][j] = D + A - B - C

        return answer
