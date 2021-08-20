class Solution:

    def convert_to_tuple(self, lst):
        if lst[0] == 0:
            return tuple(lst)
        else:
            return tuple([int(not x) for x in lst])

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        from collections import defaultdict
        row_counts = defaultdict(int)
        for row in matrix:
            row_counts[self.convert_to_tuple(row)] += 1
        return max(row_counts.values())
