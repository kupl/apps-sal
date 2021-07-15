class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if not A or len(A) < 2:
            return True
        
        self.direction = None
        
        return self.isMonotonicHelper(A, 0, len(A)-1)
    
    def isMonotonicHelper(self, A, start, end):
        if start < end:
            mid = (start + end) // 2
            if self.isMonotonicHelper(A, start, mid) and self.isMonotonicHelper(A, mid+1, end):
                if self.direction is None:
                    if A[mid] < A[mid+1]:
                        self.direction = 1
                    elif A[mid] > A[mid+1]:
                        self.direction = 0
                    return True
                elif self.direction == 1:
                    return A[mid] <= A[mid+1]
                else:
                    return A[mid] >= A[mid+1]
            else:
                return False
        return True
