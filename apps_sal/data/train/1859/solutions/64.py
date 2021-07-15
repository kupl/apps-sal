class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len( matrix)
        col = len(matrix[0])
        ret =0
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0: ret += 1
                    else:
                        matrix[r][c]= min(matrix[r-1][c-1],matrix[r-1][c],matrix[r][c-1]) + 1
                        ret += matrix[r][c]
        return ret
