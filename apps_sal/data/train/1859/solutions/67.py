# 1277. Count Square Submatrices with All Ones

def make_partial (m, n, matrix):
    ans = [[0 for __ in range (n + 1)] for _ in range (m + 1)]
    for i in range (m + 1):
        for j in range (n + 1):
            if i == 0 and j == 0:
                p = 0
            else:
                p = matrix[i-1][j-1] + ans[i-1][j] + ans[i][j-1] - ans[i-1][j-1]
            ans[i][j] = p
    return ans

def get_rect (partial, i0, j0, i1, j1):
    return partial[i1][j1] + partial[i0][j0] - partial[i0][j1] - partial[i1][j0]

def count_squares (matrix):
    m, n = len (matrix), len (matrix[0])
    partial = make_partial (m, n, matrix)

    ans = 0
    for i in range (0, m):
        for j in range (0, n):
            max_w = min (m - i, n - j)
            for w in range (1, max_w + 1):
                if get_rect (partial, i, j, i+w, j+w) == w**2:
                    ans += 1
                else:
                    break

    return ans

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        return count_squares(matrix)
