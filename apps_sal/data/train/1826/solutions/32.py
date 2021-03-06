class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        def matsum(mat, x1, y1, x2, y2):
            sumi = 0
            for row in mat[x1:x2 + 1]:
                sumi += sum(row[y1:y2 + 1])
            return sumi
        newmat = [[0] * len(row) for row in mat]
        for (ri, row) in enumerate(mat):
            for (ci, i) in enumerate(row):
                newmat[ri][ci] = matsum(mat, max(0, ri - K), max(0, ci - K), min(len(mat) - 1, ri + K), min(len(row) - 1, ci + K))
        return newmat
