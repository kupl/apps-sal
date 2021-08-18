class Solution:
    def gs(self, matrix, x, y, i, j):
        ans = matrix[i][j]
        if y:
            ans -= matrix[i][y - 1]
        if x:
            ans -= matrix[x - 1][j]
        if x and y:
            ans += matrix[x - 1][y - 1]
        return ans

    def countSquares(self, matrix: List[List[int]]) -> int:
        n: int = len(matrix)
        m = 0
        m = len(matrix[0])
        for i in range(n):
            pre = 0
            for j in range(m):
                matrix[i][j] += pre
                pre = matrix[i][j]
        for i in range(1, n):
            for j in range(m):
                matrix[i][j] += matrix[i - 1][j]
        ans = 0
        for i in range(n):
            for j in range(m):
                x, y = i, j
                l = 1
                while x >= 0 and y >= 0:
                    if l * l == self.gs(matrix, x, y, i, j):
                        ans += 1
                    else:
                        break
                    x, y, l = x - 1, y - 1, l + 1
        return ans
