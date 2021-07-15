class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if len(A)<=1:
            return A
        left=len(A)-2
        while left>=0 and A[left]<=A[left+1]:
            left-=1
        
        if left<0:
            return A
        
        right=len(A)-1
        
        while A[right]>=A[left] and right>=0:
            right-=1
        
        while right>=0 and A[right]==A[right-1]:
            right-=1
            
        A[left],A[right]=A[right],A[left]
        return A
        
    

