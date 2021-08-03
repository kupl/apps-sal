class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(1, len(A)):
            for j in range(len(A)):
                
                temp = A[i-1][j]
                A[i-1][j] = float(\"Inf\")
                A[i][j] += min(A[i-1])
                A[i-1][j] = temp
        return min(A[-1])
