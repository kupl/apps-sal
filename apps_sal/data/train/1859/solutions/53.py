class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        M = len(matrix[0])
        result = [[0 for j in range(M)] for i in range(N)]
        ss = 0
        for i in range(N):
            for j in range(M):
                if i == 0 or j == 0:
                    result[i][j] = matrix[i][j]
                else:
                    result[i][j] = matrix[i][j] * (1 + min(
                            min(result[i-1][j],
                                result[i][j-1]
                            ),
                            result[i-1][j-1],
                    ))
                ss += result[i][j]
        return ss
