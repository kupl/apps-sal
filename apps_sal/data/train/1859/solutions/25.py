class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:

        def countHelper(r: int, c: int, size: int = 0) -> int:
            if r + size >= rMax or c + size >= cMax:
                return 0
            rowOnes = rSums[r + size][c + size]
            if c > 0:
                rowOnes -= rSums[r + size][c - 1]
            colOnes = cSums[c + size][r + size]
            if r > 0:
                colOnes -= cSums[c + size][r - 1]
            return 1 + countHelper(r, c, size + 1) if rowOnes == colOnes == size + 1 else 0
        rMax = len(matrix)
        cMax = len(matrix[0])
        rSums = [[0] * cMax for _ in range(rMax)]
        cSums = [[0] * rMax for _ in range(cMax)]
        for (r, row) in enumerate(matrix):
            for (c, sq) in enumerate(row):
                rSums[r][c] = cSums[c][r] = matrix[r][c]
                if c > 0:
                    rSums[r][c] += rSums[r][c - 1]
                if r > 0:
                    cSums[c][r] += cSums[c][r - 1]
        totalSquares = 0
        for (r, row) in enumerate(matrix):
            for (c, sq) in enumerate(row):
                if sq == 1:
                    totalSquares += countHelper(r, c)
        return totalSquares
