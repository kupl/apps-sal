class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 2: return True
        
        d = A[1] - A[0]
        
        for i in range(1, len(A)-1):
            new_d = A[i+1] - A[i]
                
            if new_d * d < 0: return False
            if new_d != 0:
                d = new_d
        return True
            

