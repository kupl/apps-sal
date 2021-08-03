class Solution:
    def suma(self, mat, m, n, red, stupac, K):
        s = 0
        poc_red = max(red - K, 0)
        kraj_red = min(red + K + 1, m)

        poc_stupac = max(stupac - K, 0)
        kraj_stupac = min(stupac + K + 1, n)

        for i in range(poc_red, kraj_red):
            for j in range(poc_stupac, kraj_stupac):
                s += mat[i][j]
        return s

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = self.suma(mat, m, n, i, j, K)
        return res
