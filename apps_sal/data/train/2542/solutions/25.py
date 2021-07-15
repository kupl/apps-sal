class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        isAscending = True
        isDescending = True
        
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                isAscending = False
            if A[i] < A[i+1]:
                isDescending = False
        return isAscending or isDescending
