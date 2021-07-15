class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        positions = {}
        max_rows = 0
        for i in range(len(matrix)):
            zeros = []
            ones = []
            for j, coin in enumerate(matrix[i]):
                if coin == 0:
                    zeros.append(j)
                else:
                    ones.append(j)
            zeros = tuple(zeros)
            ones = tuple(ones)
            if 0 in zeros:
                key = (zeros, ones)
            else:
                key = (ones, zeros)
            positions[key] = positions.get(key, 0) + 1
            max_rows = max(max_rows, positions[key])
        return max_rows
