class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        decreasing = True
        increasing = True
        for i in range(0, len(A) - 1):
            if A[i] > A[i + 1]:
                decreasing = False
            if A[i] < A[i + 1]:
                increasing = False
        return decreasing or increasing
