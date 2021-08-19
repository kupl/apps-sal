class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 1:
            return True
        t = 0
        for i in range(len(A) - 1):
            if A[i] < A[i + 1] and t == -1:
                return False
            elif A[i] > A[i + 1] and t == 1:
                return False
            elif A[i] < A[i + 1] and t == 0:
                t = 1
            elif A[i] > A[i + 1] and t == 0:
                t = -1
        return True
