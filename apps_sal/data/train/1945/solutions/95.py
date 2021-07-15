class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # pattern for each row
        count = {}
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[0])):
                row.append(matrix[i][j]^matrix[i][0])
            k = ''.join(map(str, row))
            if k not in count:
                count[k] = 1
            else:
                count[k] += 1
        res = 0
        for k, v in count.items():
            res = max(res, v)
        return res
