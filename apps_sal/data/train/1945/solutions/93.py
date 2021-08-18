class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        rm = {}
        for row in matrix:
            r1 = '
            r2 = '
            if r1 in rm:
                rm[r1] += 1
            elif r2 in rm:
                rm[r2] += 1
            else:
                rm[r1] = 1
        return max(rm.values())
