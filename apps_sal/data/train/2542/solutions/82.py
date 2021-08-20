class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        inc = True
        dec = True
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                inc = False
            if A[i - 1] < A[i]:
                dec = False
        return inc or dec
