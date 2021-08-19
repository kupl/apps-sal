class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        result = 0
        A.sort()
        for i in range(1, len(A)):
            if A[i - 1] >= A[i]:
                result += A[i - 1] - A[i] + 1
                A[i] = A[i - 1] + 1
        return result
