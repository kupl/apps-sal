class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(1, len(A)):
            if A[i] == A[i - 1] or (i - 2 >= 0 and A[i] == A[i - 2]):
                return A[i]
        return A[0]
