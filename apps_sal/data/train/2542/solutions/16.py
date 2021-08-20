class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True
        i = 0
        while i < len(A) - 1 and A[i] == A[i + 1]:
            i += 1
        if i >= len(A) - 1:
            return True
        if A[i] > A[i + 1]:
            while i < len(A) - 1:
                if A[i] < A[i + 1]:
                    return False
                i += 1
            return True
        else:
            while i < len(A) - 1:
                if A[i] > A[i + 1]:
                    return False
                i += 1
            return True
