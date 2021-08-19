class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        if sorted(A) == A or sorted(A, reverse=True) == A:
            return True
        else:
            return False
