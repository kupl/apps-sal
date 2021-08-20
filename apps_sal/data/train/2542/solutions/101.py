class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 2:
            return True
        asc = None
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                continue
            if asc is None:
                asc = A[i - 1] < A[i]
            elif asc != (A[i - 1] < A[i]):
                return False
        return True
