class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        
        maxIndex = A.index(max(A))
        
        if (maxIndex == len(A)-1) or (maxIndex == 0):
            return False
        
        for i in range(maxIndex):
            if A[i] >= A[i+1]:
                return False
        
        for i in range(maxIndex, len(A)-1):
            if A[i] <= A[i+1]:
                return False
        
        return True
