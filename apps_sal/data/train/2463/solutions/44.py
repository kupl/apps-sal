class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) == 0 or len(A) == 1:
            return False
        
        idx = 0
        
        while (idx < len(A) - 1 and A[idx] < A[idx+1]):
            idx += 1
        if idx == 0 or idx == len(A) - 1:
            return False
        while (idx < len(A) - 1 and A[idx] > A[idx+1]):
            idx += 1
        
        print((idx, len(A)))
        return idx == len(A) - 1

