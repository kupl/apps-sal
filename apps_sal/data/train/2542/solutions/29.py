class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        is_asc = True
        is_desc = True
        
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                is_desc = False
            if A[i] < A[i-1]:
                is_asc = False
        
        return is_asc or is_desc
