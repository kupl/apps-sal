class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        arr = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        def addsum(i, j):
            i_start = i - k
            i_end = i + k
            j_start = j - k
            j_end = j + k
            ans = 0
            if i - k < 0:
                i_start = 0
            if i + k >= len(mat):
                i_end = len(mat) - 1
            if j - k < 0:
                j_start = 0
            if j + k >= len(mat[0]):
                j_end = len(mat[0]) - 1
            for m in range(i_start, i_end + 1):
                for n in range(j_start, j_end + 1):
                    ans += mat[m][n]
            arr[i][j] = ans
            return
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                addsum(i, j)
        return arr
