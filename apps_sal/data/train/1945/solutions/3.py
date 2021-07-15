class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
#         iMax = len(matrix)
#         jMax = matrix[0]
#         flipCounter = [0 for _ in range(jMax)]
        
        
        counterDict = defaultdict(int)
        for row in matrix:
            str0 = \"\"
            str1 = \"\"
            for num in row:
                str0 += str(num)
                str1 += str(abs(num-1))
            counterDict[str0] += 1
            counterDict[str1] += 1
        return max(counterDict.values())
