class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing = True
        for x, y in zip(A, A[1:]):
            if x > y:
                increasing = False
                break
        decreasing = True
        for x, y in zip(A, A[1:]):
            if x < y:
                decreasing = False
                break
        return increasing or decreasing
