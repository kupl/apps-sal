class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 2:
            return True
        increasing = False
        decreasing = False
        i = 0
        while i < len(A) - 1 and (not increasing and (not decreasing)):
            if A[i] == A[i + 1]:
                i += 1
                continue
            if A[i] < A[i + 1]:
                increasing = True
            else:
                decreasing = True
            i += 1
        if increasing:
            while i < len(A) - 1:
                if A[i] > A[i + 1]:
                    return False
                i += 1
            return True
        if decreasing:
            while i < len(A) - 1:
                if A[i] < A[i + 1]:
                    return False
                i += 1
            return True
        if not increasing and (not decreasing):
            return True
