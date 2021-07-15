class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        result = 0

        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                continue
            result += A[i-1]-A[i]+1
            A[i] = A[i-1]+1

        return result

