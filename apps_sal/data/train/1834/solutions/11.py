class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        w = len(A[0])
        h = len(A)
        max_row = int(2 ** w) - 1

        def max_col(ci):
            return h * c_val(ci)

        def c_val(ci):
            return 2 ** (w - ci - 1)

        row_sum = [sum(v * c_val(ci) for ci, v in enumerate(l)) for l in A]
        col_sum = [sum(A[ri][ci] * c_val(ci) for ri in range(h)) for ci in range(w)]

        flipped = True
        while flipped:
            flipped = False
            for ri, r in enumerate(row_sum):
                if r < max_row - r:
                    flipped = True
                    for ci in range(w):
                        A[ri][ci] = 1 - A[ri][ci]
                        row_sum[ri] = max_row - r
                        if A[ri][ci] == 1:
                            col_sum[ci] += c_val(ci)
                        else:
                            col_sum[ci] -= c_val(ci)
            for ci, c in enumerate(col_sum):
                if c < max_col(ci) - c:
                    flipped = True
                    for ri in range(h):
                        A[ri][ci] = 1 - A[ri][ci]
                        col_sum[ci] = max_col(ci) - c
                        if A[ri][ci] == 1:
                            row_sum[ri] += c_val(ci)
                        else:
                            row_sum[ri] -= c_val(ci)
        return sum(row_sum)
