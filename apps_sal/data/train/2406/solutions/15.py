class Solution(object):

    def peakIndexInMountainArray(self, A):
        (lo, hi) = (0, len(A) - 1)
        while lo < hi:
            mi = (lo + hi) // 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
