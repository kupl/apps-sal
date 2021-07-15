class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        squares = 0
        for i in range(0, n):
            for j in range(0, m):
                if matrix[i][j] == 1:
                    squares += self.get_squares(matrix, i, j, n, m)
        
        return squares
    
    def get_squares(self, matrix, i, j, n, m):
        count = 1
        s = 2
        while i + s <= n and j + s <= m:
            all_ones = True
            for k in range(i, i + s):
                for l in range(j, j + s):
                    if matrix[k][l] == 0:
                        return count
            count += 1
            s += 1

        return count
