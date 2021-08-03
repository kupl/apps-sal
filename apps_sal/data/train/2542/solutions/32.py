class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        dec = False
        inc = False

        for i in range(len(A) - 1):
            j = i + 1
            if A[i] is not A[j]:
                if A[i] < A[j]:
                    inc = True
                elif A[i] > A[j]:
                    dec = True
            if(inc and dec):
                return False
        return True
