class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        memo = {}
        def recursive(row, col):
            if 0 <= row < len(matrix) and 0<= col < len(matrix[0]) and matrix[row][col] == 1:
                nextRow = recursive(row+1, col)
                nextCol = recursive(row, col+1)
                nextDiag = recursive(row+1, col+1)
                return min(nextRow, nextCol, nextDiag) + 1
            return 0
        
        def cached(row, col):
            pair = (row, col)
            if pair in memo: return memo[pair]
            if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] == 1:
                nextRow = cached(row+1, col)
                nextCol = cached(row, col+1)
                nextDiag = cached(row+1, col+1)
                memo[pair] = min(nextRow, nextCol, nextDiag)+1
                return memo[pair]
            return 0
            
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                count += cached(i, j)
        return count

