class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        new_array = sorted(A)
        new_array_rev = sorted(A, reverse=True)
        
        if A == new_array or A == new_array_rev:
            return True
        else:
            return False

