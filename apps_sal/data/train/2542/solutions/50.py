class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        res1 = sorted(A, reverse=True)
        res2 = sorted(A)
        if res1 == A or res2 == A:
            return True
        return False
