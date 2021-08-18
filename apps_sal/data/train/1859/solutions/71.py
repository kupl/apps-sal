class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if(len(matrix) > 0):
            t = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
            result = 0
            for i in range(1, len(matrix) + 1):
                for j in range(1, len(matrix[0]) + 1):
                    if(matrix[i - 1][j - 1] == 0):
                        t[i][j] == 0
                    else:
                        t[i][j] = min(t[i - 1][j], t[i][j - 1], t[i - 1][j - 1]) + 1
                        result += t[i][j]
            for i in t:
                print(i)
            return result
        else:
            return 0
