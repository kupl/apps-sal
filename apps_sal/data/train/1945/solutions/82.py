class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        flips_for_row = {}
        for row in matrix:
            curr_tuple = str([i for i in range(len(row)) if row[i] == 1])
            if curr_tuple in flips_for_row:
                flips_for_row[curr_tuple] = flips_for_row[curr_tuple] + 1
            else:
                flips_for_row[curr_tuple] = 1
            curr_tuple = str([i for i in range(len(row)) if row[i] == 0])
            if curr_tuple in flips_for_row:
                flips_for_row[curr_tuple] = flips_for_row[curr_tuple] + 1
            else:
                flips_for_row[curr_tuple] = 1
        return max(flips_for_row.values())
