import time


class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        flip = []
        flip2 = []
        ma = 0
        for i in matrix:
            temp = []
            temp2 = []
            for k in range(len(i)):
                if i[k] == 0:
                    temp += [k]
                else:
                    temp2 += [k]
            flip.append(temp)
            flip2.append(temp2)
        for i in flip:
            if flip.count(i) + flip2.count(i) > ma:
                ma = flip.count(i) + flip2.count(i)
        return ma
