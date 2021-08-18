class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        while i + 1 < N and A[i] < A[i + 1]:
            i += 1

        if i == 0 or i == N - 1:
            return False

        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1
