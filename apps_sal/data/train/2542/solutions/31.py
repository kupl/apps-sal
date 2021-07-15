class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        len_ = len(A)
        
        if (len_ == 0 or len_ == 1 or len_ == 2):
            return True
        
        f, l = A[0], A[-1]
        prev = f
        
        for n in A[1:]:
            if (f < l):
                if (n < prev):
                    return False
            if (f > l):
                if (n > prev):
                    return False
            if (f == l):
                if (n != prev):
                    return False
            prev = n
        return True

