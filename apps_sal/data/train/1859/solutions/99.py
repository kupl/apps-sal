class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ansmatrix = [[0]*(m + 1) for _ in range(n+1)]
        count = 0
        
        for row in range(1, n + 1):
            for col in range(1, m + 1):
                if matrix[row - 1][col - 1] == 1:
                    ansmatrix[row][col] = 1 + min(ansmatrix[row][col - 1], ansmatrix[row - 1][col], ansmatrix[row - 1][col - 1])
                    count += ansmatrix[row][col]
                    
        return count

