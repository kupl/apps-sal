class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        cols = len(matrix[0])
        allOnes = 0
        for i in range(0, cols):
            allOnes <<= 1
            allOnes |= 1
        freq = {}
        count = 0
        for i in range(0, len(matrix)):
            rowNumber = 0
            for j in range(0, len(matrix[i])):
                rowNumber = rowNumber << 1
                rowNumber = rowNumber | matrix[i][j]
            xorRowNumber = rowNumber ^ allOnes
            if rowNumber in freq:
                freq[rowNumber] += 1
                count = max(count, freq[rowNumber])
            elif xorRowNumber in freq:
                freq[xorRowNumber] += 1
                count = max(count, freq[xorRowNumber])
            else:
                freq[rowNumber] = 1
                count = max(count, freq[rowNumber])
        return count
