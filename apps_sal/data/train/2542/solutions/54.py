class Solution(object):
    def isMonotonic(self, A):
        monotonicIncr = True
        monotonicDecr = True

        for i in range(len(A) - 1):
            j = i + 1
            if A[i] > A[j]:
                monotonicIncr = False
            if A[i] < A[j]:
                monotonicDecr = False

        return monotonicIncr or monotonicDecr
