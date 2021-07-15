import time
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        flip = []
        flip2 = []
        ma = 0
        for i in matrix:
            temp = [j for j in range(len(i)) if i[j]==0]
            temp2 = [j for j in range(len(i)) if i[j]==1]
            flip.append(temp)
            flip2.append(temp2)
        for i in flip:
            if flip.count(i)+flip2.count(i) > ma:
                ma = flip.count(i)+flip2.count(i)            
       
        return ma
