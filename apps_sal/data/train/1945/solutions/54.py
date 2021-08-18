class Solution:
    def maxEqualRowsAfterFlips(self, g: List[List[int]]) -> int:

        rows, cols, d = len(g), len(g[0]), {}
        for row in range(rows):
            vct = tuple(g[row])
            d[vct] = d.setdefault(vct, 0) + 1

        res = 0
        for vct in d:
            inv = tuple(el ^ 1 for el in vct)

            if inv in d:
                matches = d[vct] + d[inv]
            else:
                matches = d[vct]

            res = max(res, matches)
        return res
