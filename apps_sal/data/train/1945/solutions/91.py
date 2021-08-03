class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        flipper = int(''.join([str(bit) for bit in [1] * len(matrix[1])]), 2)
        bits = [int(''.join([str(bit) for bit in row]), 2) for row in matrix]

        mx = 1
        for bit1 in bits:
            count = sum(
                1 for bit in bits if bit == bit1 or bit1 ^ flipper == bit
            )

            mx = max(mx, count)

        return mx
