class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        monotonic = 2
        lenA = len(A)
        for i in range(lenA-1):
            if A[i] > A[i+1]:
                monotonic -= 1
                break
        for i in range(lenA-1):
            if A[i] < A[i+1]:
                monotonic -= 1
                break
        return monotonic
