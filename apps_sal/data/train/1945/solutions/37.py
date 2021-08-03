class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def reverse_row(row):
            res = [0] * len(row)
            for i, val in enumerate(row):
                res[i] = 1 - row[i]
            return res

        d = {}
        for row in matrix:
            rev_row = reverse_row(row)

            if tuple(row) in d:
                d[tuple(row)] += 1
            elif tuple(rev_row) in d:
                d[tuple(rev_row)] += 1
            else:
                d[tuple(row)] = 1

        res = sorted(d.items(), key=lambda x: x[1], reverse=1)
        return res[0][1]
