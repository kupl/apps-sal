class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        rm = {}
        for row in matrix:
            r1 = '#'.join([str(x) for x in row])
            r2 = '#'.join([('1' if x == 0 else '0') for x in row])
            if r1 in rm:
                rm[r1] += 1
            elif r2 in rm:
                rm[r2] += 1
            else:
                # r1 not in rm and r2 not in rm
                rm[r1] = 1
        return max(rm.values())
