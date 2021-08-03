class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hashTab = defaultdict(int)

        rows, cols = len(matrix), len(matrix[0])

        allOnes = int('1' * cols, 2)

        maxSizeGroup = 0

        for row in matrix:
            val = reduce(lambda a, x: a << 1 ^ x, row)

            if val not in hashTab:
                val ^= allOnes

            hashTab[val] += 1
            maxSizeGroup = max(maxSizeGroup, hashTab[val])

        return maxSizeGroup
