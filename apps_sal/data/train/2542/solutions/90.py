class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = True
        dec = True
        for i in range(len(A)-1):
            if A[i+1] - A[i] > 0:
                inc = inc and True
                dec = False
            elif A[i+1] - A[i] < 0:
                dec = dec and True
                inc = False
                
        return inc or dec
