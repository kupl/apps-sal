class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        hori = [row[:] for row in matrix]
        vert = [row[:] for row in matrix]
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            s = 0
            for j in range(C):
                if matrix[i][j]:
                    s += matrix[i][j]
                else:
                    s = 0
                hori[i][j] = s
        for j in range(C):
            s = 0
            for i in range(R):
                if matrix[i][j]:
                    s += matrix[i][j]
                else:
                    s = 0
                vert[i][j] = s
        out = 0
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 1:
                    if i - 1 < 0 or j - 1 < 0:
                        out += 1
                        continue
                    if matrix[i - 1][j - 1] == 0:
                        out += 1
                        continue
                    x = int(matrix[i - 1][j - 1]**0.5)
                    a = min([x, hori[i][j - 1], vert[i - 1][j]])
                    out += a + 1
                    matrix[i][j] = (a + 1)**2
        return out
