class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        asc_arr = sorted(A)
        desc_arr = sorted(A, reverse=True)
        return (A == asc_arr or A == desc_arr)
