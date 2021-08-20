class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        dec = False
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                dec = True
        for i in range(len(A) - 1):
            if A[i] > A[i + 1] and dec:
                return False
        return True
