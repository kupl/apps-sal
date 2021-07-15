class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r,c = len(matrix),len(matrix[0])
        count = 0 
        for i in range(r):
            for j in range(c) :
                if matrix[i][j] == 1 :
                    if i == 0 or j == 0:
                        count += 1
                    else :
                        cell_val = min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j]) + matrix[i][j]
                        count += cell_val
                        matrix[i][j] = cell_val
        return count
