class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        res = 0
        for i in range(len(A)):
            if i > 0 and A[i] <= A[i - 1]:
                res += A[i - 1] + 1 - A[i]
                A[i] += A[i - 1] + 1 - A[i]
        return res
