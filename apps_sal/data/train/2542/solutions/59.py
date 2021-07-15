class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        B=A.copy()
        A.sort()
        if A==B or A[::-1]==B:
            return True
        return False

