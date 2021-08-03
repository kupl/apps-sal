def isMono(A, forward=True):
    curValue = A[0]

    for i in range(1, len(A)):
        if forward and A[i] < curValue:
            return False
        if not forward and A[i] > curValue:
            return False

        curValue = A[i]

    return True


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return isMono(A) or isMono(A, False)
