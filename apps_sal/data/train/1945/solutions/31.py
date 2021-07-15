class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        noninv = {}
        
        for row in matrix:
            row = repr(row)
            if row in noninv:
                noninv[row] += 1
            else:
                noninv[row] = 1
            
        count = 0
        for row in matrix:
            revrow = [i^1 for i in row]
            revrow = repr(revrow)
            row = repr(row)
            
            if revrow in noninv:
                count = max(count, noninv[row] + noninv[revrow])
            else:
                count = max(count, noninv[row])
            
        return count
        

