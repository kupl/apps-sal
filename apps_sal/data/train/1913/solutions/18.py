class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        if n<=1: return A
        
        # moving left pointer
        left = n - 2
        while left >= 0 and A[left] <= A[left+1]:
            left -= 1
        if left < 0:
            return A
        
        # moving right pointer
        right = n-1
        while A[right] >= A[left]:
            right -= 1
        while A[right] == A[right-1]:
            right -= 1
            
        # swap left and right
        A[left],A[right] = A[right],A[left]
        
        return A

