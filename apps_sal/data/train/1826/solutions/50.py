class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for r in range(m):
            mat[r] = [0] * K + mat[r] + [0] * K
        for i in range(K):
            mat = [[0] * (n + 2 * K)] + mat + [[0] * (n + 2 * K)]
        ret = []
        print(mat)
        for i in range(m):
            this = []
            for j in range(n):
                I, J = i + K, j + K
                add = sum([sum(mat[r][J - K:J + K + 1]) for r in range(I - K, I + K + 1)])
                # print(mat[r][J-K:J+K])
                this.append(add)
                # this.append(sum([sum(mat[r][c] for c in range(J-K, J+K)) for r in range(I-K, I+K)]))
            ret.append(this)
        return ret
