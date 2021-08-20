class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        if A[-1] > A[0]:
            inc = True
            for i in range(0, len(A) - 1):
                if A[i] > A[i + 1]:
                    return False
            else:
                return True
        else:
            dec = True
            for i in range(0, len(A) - 1):
                if A[i] < A[i + 1]:
                    return False
            else:
                return True
