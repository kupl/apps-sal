class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        a1, a2 = sorted(A), sorted(A, reverse = True)
        if A == a1 or A == a2:
            return True
        return False
        '''
        nD, nI = 1, 1
        for i in range(1, len(A)):
            if A[i] - A[i-1] < 0:
                nD = 0
            elif A[i] - A[i-1] > 0 :
                nI = 0
        return nI or nD
        '''
