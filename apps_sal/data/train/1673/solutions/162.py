class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:

        if len(A) == 1:
            return min(A[0])

        for i in range(1, len(A)):

            minValue, minIdx = sys.maxsize, -1
            secondMinValue = sys.maxsize
            for j in range(len(A[0])):
                if A[i - 1][j] < minValue:
                    secondMinValue = minValue
                    minValue, minIdx = A[i - 1][j], j
                elif A[i - 1][j] < secondMinValue:
                    secondMinValue = A[i - 1][j]
            for j in range(len(A[0])):
                if j == minIdx:
                    A[i][j] += secondMinValue
                else:
                    A[i][j] += minValue

        return min(A[-1])
