class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        sort = sorted(A)
        return A==sort or A[::-1]==sort
