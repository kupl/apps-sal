class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        sq = 0
        m_row = range(len(matrix))
        m_col = range(len(matrix[0]))

        def expand_square(row, n, m, p, square=0, count=1):
            while count > -1:
                for i in range(count):
                    if row + i == m:
                        return square
                    for j in range(count):
                        if n + j == p:
                            return square
                        elif matrix[row + i][n + j] != 1:
                            return square
                square += 1
                count += 1

        for row in m_row:
            for n in m_col:
                if matrix[row][n] == 1:
                    sq += expand_square(row, n, len(matrix), len(matrix[0]))

        return sq
