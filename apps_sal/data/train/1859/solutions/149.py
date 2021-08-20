class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        A = matrix
        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
        return sum([A[i][j] for i in range(len(A)) for j in range(len(A[0]))])
