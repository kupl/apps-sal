class Solution:

    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(len(A) - 1):
            x = [0 for _ in A]
            for j in range(len(A)):
                ls = []
                for k in range(len(A)):
                    if not j == k:
                        ls.append(A[0][k])
                x[j] = A[i + 1][j] + min(ls)
            A[0] = x
        return min(A[0])
