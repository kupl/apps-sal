class Solution:

    def largest1BorderedSquare(self, A: List[List[int]]) -> int:
        (n, m) = (len(A), len(A[0]))
        (V, H) = ([[0] * m for _ in range(n)], [[0] * m for _ in range(n)])
        for col in range(m):
            for row in range(n):
                if row == 0:
                    V[row][col] = A[row][col]
                else:
                    V[row][col] = 0 if A[row][col] == 0 else V[row - 1][col] + 1
        for row in range(n):
            for col in range(m):
                if col == 0:
                    H[row][col] = A[row][col]
                else:
                    H[row][col] = 0 if A[row][col] == 0 else H[row][col - 1] + 1
        res = 0
        for row in range(n):
            for col in range(m):
                small = min(H[row][col], V[row][col])
                while small > res:
                    if V[row][col - small + 1] >= small and H[row - small + 1][col] >= small:
                        res = small
                        break
                    small -= 1
        return res * res
