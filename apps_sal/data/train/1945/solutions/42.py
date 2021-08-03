class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        columnsToFlipOneForEqualRow = {}
        columnsToFlipZeroForEqualRow = {}
        self.height = len(matrix)
        self.width = len(matrix[0])

        for y in range(self.height):
            row = matrix[y]
            columnsToFlipOneForEqualRow[y] = []
            columnsToFlipZeroForEqualRow[y] = []

            for x in range(self.width):
                element = row[x]

                if element == 0:
                    columnsToFlipOneForEqualRow[y].append(x)
                else:
                    columnsToFlipZeroForEqualRow[y].append(x)

        patterns = {}

        for index in range(self.height):
            first = str(columnsToFlipOneForEqualRow[index])
            second = str(columnsToFlipZeroForEqualRow[index])

            if first not in patterns:
                patterns[first] = 0

            if second not in patterns:
                patterns[second] = 0

            patterns[first] += 1
            patterns[second] += 1

        return max(patterns.values())
