class Solution:
    numRows = 0
    numCols = 0
    mat = [[]]
    K = 0

    def getBounds(self, row, col):
        return [(max(row - self.K, 0), max(col - self.K, 0)), (min(row + self.K, self.numRows - 1), min(col + self.K, self.numCols - 1))]

    def getBlockSum(self, bounds):
        ret = 0
        rowRestricted = self.mat[bounds[0][0]:bounds[1][0] + 1]
        for row in rowRestricted:
            ret += sum(row[bounds[0][1]:bounds[1][1] + 1])
        return ret

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        ret = []
        self.numRows = len(mat)
        self.numCols = len(mat[0])
        self.mat = mat
        self.K = K
        for row in range(self.numRows):
            tmpRow = []
            for col in range(self.numCols):
                bounds = self.getBounds(row, col)
                tmpRow.append(self.getBlockSum(bounds))
            ret.append(tmpRow)
        return ret
