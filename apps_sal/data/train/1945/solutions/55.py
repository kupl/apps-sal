class Solution:
    def maxEqualRowsAfterFlips(self, g: List[List[int]]) -> int:
        # want to find number of rows that are identical or exactly opposite
        # i.e. after flipping cols these can be all 1's or all 0's

        # pass 1: iterate grid rows
        # store vectors in dict hashmap {vector : freq}
        # pass 2: iterate grid rows
        # create inverse (XOR), check frequency of exact match + inverse
        # take the max over all rows, return
        # O(M + MN) time, O(M) space

        rows, cols, d = len(g), len(g[0]), {}

        for row in range(rows):
            vct = tuple(g[row])
            d[vct] = d.setdefault(vct, 0) + 1

        res = 0
        for row in range(rows):
            vct = tuple(g[row])
            inv = tuple(el ^ 1 for el in g[row])

            matches = 0
            if vct in d:
                matches += d[vct]
            if inv in d:
                matches += d[inv]

            res = max(res, matches)
        return res
