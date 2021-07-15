class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        groups = {}
        for row in matrix:
            tuple_row = tuple(row)
            if tuple_row not in groups:
                groups[tuple_row] = 1
            else:
                groups[tuple_row] += 1
        max_equal = 0
        for row in groups.keys():
            rev_row = tuple([1-x for x in row])
            group_max = groups[row]
            if row != rev_row and rev_row in groups:
                group_max += groups[rev_row]
            max_equal = max(max_equal, group_max)
            
        return max_equal
