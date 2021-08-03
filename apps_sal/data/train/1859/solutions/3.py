class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        size = 1
        maxSize = min(len(matrix), len(matrix[0]))
        prevInd = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    count += 1
                    prevInd.append([i, j])
        while size <= maxSize and prevInd:
            newInd = []
            for ind in prevInd:
                row = ind[0]
                col = ind[1]
                add = True
                if row + size < len(matrix) and col + size < len(matrix[0]):
                    for r in range(row, row + size + 1):
                        if not matrix[r][col + size]:
                            add = False
                            break
                    for c in range(col, col + size + 1):
                        if not matrix[row + size][c]:
                            add = False
                            break
                    if add:
                        count += 1
                        newInd.append([row, col])
            prevInd = newInd
            size += 1
        return count
