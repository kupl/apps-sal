class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = False
        i = 0
        while i < len(A) - 1 and A[i] == A[i + 1]:
            i += 1
        if i == len(A) - 1:
            return True
        if A[i] < A[i + 1]:
            inc = True

        for i in range(1, len(A) - 1):
            if inc == True:
                if A[i] > A[i + 1]:
                    return False
            if inc == False:
                if A[i + 1] > A[i]:
                    return False
        return True
