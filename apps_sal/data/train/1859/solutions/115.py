class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        result = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    idx = 1
                    isTrue = True
                    while isTrue and r + idx != rows and (c + idx != cols):
                        for h in range(idx + 1):
                            if matrix[r + idx][c + h] != 1 or matrix[r + h][c + idx] != 1:
                                isTrue = False
                                break
                        if isTrue:
                            idx += 1
                    result += idx
        return result
