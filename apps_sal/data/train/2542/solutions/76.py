class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 2:
            return True
        
        increasing = None
        previous = A[0]
        for element in A[1:]:
            if increasing == True and element < previous:
                return False
            
            if increasing == False and element > previous:
                return False
            
            if increasing is None and element != previous:
                increasing = element > previous
            
            previous = element
            
        return True

