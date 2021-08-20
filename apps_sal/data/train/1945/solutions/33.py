from collections import defaultdict


class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """
        # Analysis:


        """
        lookup = collections.defaultdict(int)
        for row in matrix:
            vals = []
            trans = []
            for c in row:
                vals.append(c)
                trans.append(1 - c)
            lookup[str(vals)] += 1
            lookup[str(trans)] += 1
        return max(lookup.values())
