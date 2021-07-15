class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increase, decrease = True, True
        
        for i in range(1, len(A)):
            if A[i-1] > A[i]:
                increase = False
                
            if A[i-1] < A[i]:
                decrease = False
                
        return increase or decrease
    

