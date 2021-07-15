class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i=1
        N=len(A)
        if N<3:
            return False
        while(i<N and A[i]>A[i-1]):
            i +=1
        if(i==1 or i==N):
            return False
        while(i<N and A[i]<A[i-1]):
            i +=1
        return i==N  
