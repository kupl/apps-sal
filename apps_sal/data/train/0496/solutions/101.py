class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        rez = 0
        for index in range(1, len(A)):
            if A[index - 1] >= A[index]:
                rez += A[index - 1] - A[index] + 1
                A[index] = A[index - 1] + 1
        return rez
