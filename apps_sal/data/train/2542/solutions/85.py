class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        monotone = 0
        for i in range(len(A)-1):
            m = A[i+1]-A[i]
            if m*monotone<0:
                return False
            if monotone == 0 and m != 0:
                monotone = 1 if m>0 else -1
        return True
