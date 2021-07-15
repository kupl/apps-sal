class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        res = 0
        n, m = len(matrix), len(matrix[0])
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0: continue
                if r == 0 or c == 0: res += 1; continue
                matrix[r][c] = min(matrix[r-1][c-1], matrix[r][c-1], matrix[r-1][c]) + 1
                res += matrix[r][c]
        return res

