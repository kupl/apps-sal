class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        length = len(A)
        monotone_inc = True
        monotone_dec = True
        for i in range(length-1):
            if A[i+1] >= A[i]:
                continue
            else:
                monotone_inc = False
        for i in range(length-1):
            if A[i+1] <= A[i]:
                continue
            else:
                monotone_dec = False
        return monotone_inc or monotone_dec
        

