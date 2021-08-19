class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        is_asc = True
        is_desc = True
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                is_asc = False
            if A[i] < A[i + 1]:
                is_desc = False
        return is_asc or is_desc
