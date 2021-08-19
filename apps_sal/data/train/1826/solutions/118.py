class Solution:

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        (m, n) = (len(mat), len(mat[0]))
        arr = [[0 for i in range(n + 1)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                arr[i][j + 1] = arr[i][j] + mat[i][j]
        narr = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                (x1, x2, y1, y2) = (max(0, j - k), min(n - 1, j + k), max(0, i - k), min(m - 1, i + k))
                a = 0
                for t in range(y1, y2 + 1):
                    a += arr[t][x2 + 1] - arr[t][x1]
                narr[i][j] = a
        return narr
