class Solution:

    def maxEqualRowsAfterFlips(self, g: List[List[int]]) -> int:
        (rows, cols, d) = (len(g), len(g[0]), {})
        for row in range(rows):
            vct = tuple(g[row])
            d[vct] = d.setdefault(vct, 0) + 1
        res = 0
        for row in range(rows):
            vct = tuple(g[row])
            inv = tuple((el ^ 1 for el in g[row]))
            matches = 0
            if vct in d:
                matches += d[vct]
            if inv in d:
                matches += d[inv]
            res = max(res, matches)
        return res
