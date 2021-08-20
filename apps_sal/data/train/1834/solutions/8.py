class Solution:

    def matrixScore(self, A: List[List[int]]) -> int:
        total = 0
        for i in range(len(A)):
            if A[i][0] == 0:
                for j in range(len(A[0])):
                    A[i][j] = 1 - A[i][j]
        for i in range(len(A[0])):
            colZero = 0
            colOne = 0
            for j in range(len(A)):
                if A[j][i] == 1:
                    colOne += 1
                else:
                    colZero += 1
            total += max(colOne, colZero) * 2 ** (len(A[0]) - 1 - i)
        return total
