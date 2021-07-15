class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing = None
        for i in range(1, len(A)):
            if increasing is None:
                if A[i] != A[i - 1]:
                    increasing = A[i] > A[i - 1]
            elif increasing and A[i] < A[i - 1]:
                return False
            elif not increasing and A[i] > A[i - 1]:
                return False
        return True
