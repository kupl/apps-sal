class Solution:

    def repeatedNTimes(self, A):
        for i in range(len(A)):
            if A[i - 1] == A[i] or A[i - 2] == A[i]:
                return A[i]
        return A[0]
