class Solution:

    def isMonotonic(self, A):
        is_monotonic_asc = True
        is_monotonic_desc = True
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                is_monotonic_asc = False
            if A[i] > A[i - 1]:
                is_monotonic_desc = False
        return is_monotonic_asc or is_monotonic_desc
