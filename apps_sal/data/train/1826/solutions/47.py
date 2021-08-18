class Solution:
    def distk(self, k, rowsum, colsum, i, j):
        s = 0
        m = len(rowsum)
        n = len(rowsum[0])
        if(i - k >= 0):
            l = max(-1, j - k - 1)
            h = min(n - 1, j + k)
            s += rowsum[i - k][h]
            if(l > -1):
                s -= rowsum[i - k][l]

        if(i + k < m):
            l = max(-1, j - k - 1)
            h = min(n - 1, j + k)
            s += rowsum[i + k][h]
            if(l > -1):
                s -= rowsum[i + k][l]

        if(j - k >= 0):
            l = max(-1, i - k)
            h = min(m - 1, i + k - 1)
            s += colsum[h][j - k]
            if(l > -1):
                s -= colsum[l][j - k]

        if(j + k < n):
            l = max(-1, i - k)
            h = min(m - 1, i + k - 1)
            s += colsum[h][j + k]
            if(l > -1):
                s -= colsum[l][j + k]

        return s

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if(K <= 0):
            return mat
        rowsum = [[0 for i in range(n)] for j in range(m)]
        colsum = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            rowsum[i][0] = mat[i][0]
            for j in range(1, n):
                rowsum[i][j] += rowsum[i][j - 1] + mat[i][j]
        for i in range(n):
            colsum[0][i] = mat[0][i]
            for j in range(1, m):
                colsum[j][i] += colsum[j - 1][i] + mat[j][i]
        ans = [[mat[j][i] for i in range(n)] for j in range(m)]

        for k in range(1, K + 1):
            for i in range(m):
                for j in range(n):
                    x = self.distk(k, rowsum, colsum, i, j)

                    ans[i][j] += x
        return ans
