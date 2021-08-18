class Solution:
    def validMountainArray(self, A: List[int]) -> bool:

        N = len(A) - 1
        i = 0

        while i < N and A[i] < A[i + 1]:
            i += 1

        if i == 0 or i == N:
            return False

        while i < N and A[i] > A[i + 1]:
            i += 1

        return i == N
