class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        sqrsCnt = 0
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                i, j = x, y
                while True:
                    if i < 0 or j < 0: break
                    if any(matrix[j][a] != 1 for a in range(i,x+1)): break
                    if any(matrix[b][i] != 1 for b in range(j,y+1)): break
                    if matrix[j][i] != 1: break
                    sqrsCnt += 1
                    i, j = i-1, j-1
        return sqrsCnt
