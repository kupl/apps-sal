class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        vertMemo = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        horizMemo = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        diagMemo = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        squareMemo = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        if matrix[0][0] == 1:
            vertMemo[0][0] = 1
            diagMemo[0][0] = 1
            horizMemo[0][0] = 1
            squareMemo[0][0] = 1

        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 1:
                vertMemo[0][i] = 1
                diagMemo[0][i] = 1
                squareMemo[0][i] = 1
                horizMemo[0][i] = horizMemo[0][i - 1] + 1

        for i in range(1, len(matrix)):
            if matrix[i][0] == 1:
                vertMemo[i][0] = vertMemo[i - 1][0] + 1
                diagMemo[i][0] = 1
                squareMemo[i][0] = 1
                horizMemo[i][0] = 1
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    vertMemo[i][j] = vertMemo[i - 1][j] + 1
                    horizMemo[i][j] = horizMemo[i][j - 1] + 1
                    diagMemo[i][j] = diagMemo[i - 1][j - 1] + 1
                    squareMemo[i][j] = min(squareMemo[i - 1][j - 1] + 1, vertMemo[i][j], horizMemo[i][j])
        print(squareMemo)
        totSquares = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if squareMemo[i][j] != 0:
                    totSquares += squareMemo[i][j]
        return totSquares
