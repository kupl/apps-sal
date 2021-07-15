class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        M, N = len(matrix), len(matrix[0])
        if M == 1 or N == 1: return 1
        for m in range(1, M):
            for n in range(1, N):
                if matrix[m][n] == 1:
                    if matrix[m-1][n] == matrix[m][n-1] == matrix[m-1][n-1]:
                        matrix[m][n] = matrix[m-1][n-1] + 1
                    else:
                        matrix[m][n] = max(min(matrix[m-1][n], matrix[m][n-1], matrix[m-1][n-1])+1, matrix[m][n]);
                
        return sum(sum(matrix, []))

