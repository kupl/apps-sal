class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        firstcell = matrix[0][0]
        vals = {}

        for row in matrix:
            firstrowcell = row[0]
            mark = [0, 0]
            mark[firstrowcell] = firstcell
            mark[1 - firstrowcell] = 1 - firstcell

            num = 0
            for cell in row:
                num = num * 2 + mark[cell]

            vals[num] = 1 + vals.get(num, 0)

        maxcount = 0
        for val, count in vals.items():
            maxcount = max(count, maxcount)

        return maxcount
