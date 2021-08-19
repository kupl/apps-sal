class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        increasing = decreasing = True
        for (i, value) in enumerate(A):
            if i:
                if value > A[i - 1]:
                    increasing = False
                if value < A[i - 1]:
                    decreasing = False
            if not increasing and (not decreasing):
                return False
        return True
