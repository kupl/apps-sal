class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        (inc, dec) = (True, True)
        for i in range(len(A) - 1):
            if A[i + 1] > A[i]:
                dec = False
            if A[i + 1] < A[i]:
                inc = False
        return inc or dec
