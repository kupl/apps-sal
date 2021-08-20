class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 0:
            return False
        if len(A) == 1:
            return True
        incr = 0
        for i in range(1, len(A)):
            if A[i] - A[i - 1] > 0 and incr == 0:
                incr = 1
            elif A[i] - A[i - 1] > 0 and incr == -1:
                return False
            elif A[i] - A[i - 1] < 0 and incr == 0:
                incr = -1
            elif A[i] - A[i - 1] < 0 and incr == 1:
                return False
        return True
