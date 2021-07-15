class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cntMap = collections.Counter()
        flipper = {1: 0, 0: 1}
        max_val = 0
        for row in matrix:
            r, tran = \"\", \"\"
            for k in row:
                r += str(k)
                tran += str(flipper[k])
            key = r
            cntMap[r] += 1
            cntMap[tran] += 1
            max_val = max(max_val, cntMap[r])
            max_val = max(max_val, cntMap[tran])

        return max_val
                
        
