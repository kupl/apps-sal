class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        A.sort()
        result = 0
        for i in range(1,len(A)):
            result += max(0, A[i-1] - A[i] + 1)
            A[i] += max(0, A[i-1] - A[i] + 1)
        return result
