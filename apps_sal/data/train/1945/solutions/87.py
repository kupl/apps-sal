class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ma = 0
        for i in matrix:
            flip = [1-x for x in i]
            c=0
            for j in matrix:
                if j == i or j == flip:
                    c+=1            
            if c > ma:
                ma = c
       
        return ma
