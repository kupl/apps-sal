class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        A = arr
        for i in range(1, len(A)):
            for j in range(len(A[0])):
                if j == 0:
                    A[i][j] += min([A[i - 1][j] for j in range(1, len(A))])
                elif j == len(A[0]) - 1:
                    A[i][j] += min([A[i - 1][j] for j in range(0, len(A) - 1)])
                else:
                    A[i][j] += min([A[i - 1][j] for j in [x for x in range(len(A)) if x != j]])
        return min(A[-1])
