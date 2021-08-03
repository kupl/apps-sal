class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        diag = 1
        square = [matrix[i][:] for i in range(m)]
        old_rec = [(0, 0)] * m
        new_rec = [(0, 0)] * m
        old_rec[0] = matrix[0][0], matrix[0][0]
        total = matrix[0][0]
        r, c = 0, 1
        while diag < m + n - 1:
            if 0 <= r < m and 0 <= c < n:
                if matrix[r][c] == 0:
                    new_rec[r] = 0, 0
                elif r == 0:
                    new_rec[r] = (old_rec[r][0] + 1, 1)
                elif c == 0:
                    new_rec[r] = (1, old_rec[r - 1][1] + 1)
                else:
                    above_h = old_rec[r - 1][1]
                    left_w = old_rec[r][0]
                    new_rec[r] = left_w + 1, above_h + 1
                    square[r][c] += min(left_w, above_h, square[r - 1][c - 1])
                total += square[r][c]

            r += 1
            c -= 1
            if (r > m) or (c < 0):
                new_rec, old_rec = old_rec, new_rec
                diag += 1
                r = 0 if diag < n else diag - n + 1
                c = diag - r
        return total
