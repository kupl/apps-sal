class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        res = 0
        M = len(matrix)
        N = len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    continue
                if i == 0 or j == 0:
                    res += 1
                else:
                    add = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                    res += add
                    matrix[i][j] = add
        return res
