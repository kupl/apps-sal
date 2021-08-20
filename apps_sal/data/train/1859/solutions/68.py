class Solution:

    def dobra(self, x, i, j, red_matrice):
        for k in range(i, i + red_matrice):
            for l in range(j, j + red_matrice):
                if x[k][l] == 0:
                    return False
        return True

    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                for red_matrice in range(1, min(m, n) + 1):
                    if i + red_matrice <= m and j + red_matrice <= n:
                        if self.dobra(matrix, i, j, red_matrice):
                            res += 1
                        else:
                            break
        return res
