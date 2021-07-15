class Solution:
\tdef countSquares(self, matrix: List[List[int]]) -> int:
\t\tfor r in range(len(matrix)):
\t\t\tfor c in range(len(matrix[0])):
\t\t\t\tif matrix[r][c] == 1:
\t\t\t\t\tif r == 0 or c == 0:
\t\t\t\t\t\tmatrix[r][c] = 1
\t\t\t\t\telse:
\t\t\t\t\t\tmatrix[r][c] = 1 + min(matrix[r - 1][c - 1], matrix[r - 1][c], matrix[r][c - 1])

\t\treturn sum(sum(matrix, []))
