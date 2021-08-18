class Solution:

    def paint(self, A, i, j):
        if i >= len(A) or i < 0 or j < 0 or j >= len(A[0]) or A[i][j] == 0 or A[i][j] == 2:
            return
        A[i][j] = 2
        for nb in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self.paint(A, i + nb[0], j + nb[1])

    def expand(self, A, i, j, color):
        if i >= len(A) or i < 0 or j < 0 or j >= len(A[0]):
            return False
        if A[i][j] == 0:
            A[i][j] = color + 1
        return A[i][j] == 1

    def shortestBridge(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        m, n, flag = len(A), len(A[0]), False

        for i in range(m):
            if flag:
                break
            for j in range(n):
                if A[i][j] == 1:
                    self.paint(A, i, j)
                    flag = True
                    break

        for color in range(2, 2 + m + n + 1):
            for i in range(m):
                for j in range(n):
                    if A[i][j] == color and (self.expand(A, i - 1, j, color) or self.expand(A, i, j + 1, color)
                                             or self.expand(A, i + 1, j, color) or self.expand(A, i  , j-1, color)):
                        return color - 2
