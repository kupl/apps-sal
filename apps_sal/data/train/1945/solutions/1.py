class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_dict = {}
        for row in matrix:
            if row[0] == 0:
                key = tuple(row)
            else:
                newrow = [1-x for x in row]
                key = tuple(newrow)
            if key in pattern_dict:
                pattern_dict[key] += 1
            else:
                pattern_dict[key] = 1
        maxnum = 0
        for _, num in pattern_dict.items():
            maxnum = max(maxnum, num)
        return maxnum
