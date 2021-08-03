class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        def getSum(i, j):
            ii = max(i - K, 0)
            s = 0
            while ii <= min(i + K, len(mat) - 1):
                jj = max(j - K, 0)
                while jj <= min(j + K, len(mat[0]) - 1):
                    s += mat[ii][jj]
                    jj += 1
                ii += 1
            return s

        def editCol(i, j, s):
            if j - K - 1 >= 0:
                ii = max(i - K, 0)
                while ii <= min(i + K, len(mat) - 1):
                    s -= mat[ii][j - K - 1]
                    ii += 1
            if j + K < len(mat[0]):
                ii = max(i - K, 0)
                while ii <= min(i + K, len(mat) - 1):
                    s += mat[ii][j + K]
                    ii += 1
            return s

        rett = []
        for i in range(len(mat)):
            s = getSum(i, 0)
            ret = [s]
            for j in range(1, len(mat[i])):
                s = editCol(i, j, s)
                ret.append(s)
            rett.append(ret)
        return rett
