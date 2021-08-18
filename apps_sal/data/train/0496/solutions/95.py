class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        count = 0

        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                residual = A[i - 1] - A[i] + 1
                A[i] += residual
                count += residual

        return count
