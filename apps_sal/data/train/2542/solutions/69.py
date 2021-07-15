class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if not A: return True
        isIncrementing, prev = None, A[0]
        for i in range(1,len(A)):
            print(prev,A[i],isIncrementing)
            if prev < A[i] and isIncrementing == False: return False
            if prev > A[i] and isIncrementing == True:  return False
            if prev < A[i]: isIncrementing = True
            if prev > A[i]: isIncrementing = False
            prev = A[i]
        return True
