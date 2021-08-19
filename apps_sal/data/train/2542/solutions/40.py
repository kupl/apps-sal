class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        increasing = decreasing = True
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                increasing = False
            if A[i] < A[i + 1]:
                decreasing = False
        if increasing or decreasing:
            return increasing or decreasing
