class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        asc = True
        dsc = True
        for i in range(1,len(A)):
            if A[i-1]<A[i]:
                dsc=False
            elif A[i-1]>A[i]:
                asc=False
        return asc or dsc

