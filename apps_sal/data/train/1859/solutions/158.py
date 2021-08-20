class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        mat = deepcopy(matrix)
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if mat[i][j] == 0:
                    continue
                if i - 1 >= 0:
                    top = mat[i - 1][j]
                else:
                    top = 0
                if j - 1 >= 0:
                    left = mat[i][j - 1]
                else:
                    left = -1
                if i - 1 < 0 and j - 1 < 0:
                    top_left = -1
                else:
                    top_left = mat[i - 1][j - 1]
                if top_left > 0 and left > 0 and (top > 0):
                    mat[i][j] = min(top_left, left, top) + 1
        ret = 0
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                ret += mat[i][j]
        return ret
