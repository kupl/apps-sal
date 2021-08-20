class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat:
            return
        m = len(mat)
        n = len(mat[0])
        sumMat = [[0 for i in range(n)] for j in range(m)]
        verMat = [[0 for i in range(n)] for j in range(m)]
        ansMat = [[0 for i in range(n)] for j in range(m)]
        fnlMat = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            running_sum = 0
            for j in range(n):
                running_sum += mat[i][j]
                sumMat[i][j] = running_sum
        for i in range(m):
            for j in range(n):
                verMat[i][j] = self.sumRowWindow(sumMat, i, j, K)
        for j in range(n):
            running_sum = 0
            for i in range(m):
                running_sum += verMat[i][j]
                ansMat[i][j] = running_sum
        for i in range(m):
            for j in range(n):
                fnlMat[i][j] = self.sumColWindow(ansMat, i, j, K)
        return fnlMat

    def sumColWindow(self, verMat, row_i, col_j, window_k):
        col = [verMat[i][col_j] for i in range(len(verMat))]
        window_left = max(-1, row_i - window_k - 1)
        window_right = min(len(col) - 1, row_i + window_k)
        if window_left == -1:
            return col[window_right]
        return col[window_right] - col[window_left]

    def sumRowWindow(self, sumMat, row_i, col_j, window_k):
        row = sumMat[row_i]
        window_left = max(-1, col_j - window_k - 1)
        window_right = min(len(row) - 1, col_j + window_k)
        if window_left == -1:
            return row[window_right]
        return row[window_right] - row[window_left]
