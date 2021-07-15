class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        result = [matrix[0]]
        
        for i in range(1, len(matrix)):
            row = [matrix[i][0]]
            result.append(row)
            for j in range(1, len(matrix[i])):
                if not matrix[i][j]:
                    row.append(0)
                else:
                    row.append(1 + min(result[i-1][j], result[i][j-1], result[i-1][j-1]))
        return sum(sum(r) for r in result)
