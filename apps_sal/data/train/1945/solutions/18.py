class Solution:
    def maxEqualRowsAfterFlips(self, mat: List[List[int]]) -> int:

        dic = defaultdict(lambda: 0)
        for r in range(len(mat)):
            row = mat[r]
            ones = 0
            zeros = 0
            for i in range(len(row)):
                if row[i] == 0:
                    ones = ones << 1
                    zeros = zeros << 1
                    ones |= 1
                else:
                    zeros = zeros << 1
                    ones = ones << 1
                    zeros |= 1
            dic[zeros] += 1
            dic[ones] += 1
        return max(dic.values())
