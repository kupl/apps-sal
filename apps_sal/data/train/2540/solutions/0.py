class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        
        A.sort(reverse=True)
        la=len(A)
        for i in range(la-2):
            if A[i]<A[i+1]+A[i+2]:
                return A[i]+A[i+1]+A[i+2]
        return 0
