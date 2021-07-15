class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        icounter = 0
        dcounter = 0
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                dcounter += 1
            if A[i] < A[i+1]:
                icounter += 1
            if A[i] == A[i+1]:
                icounter += 1
                dcounter += 1
        if icounter == len(A) - 1 or dcounter == len(A) - 1:
            return True
        return False

