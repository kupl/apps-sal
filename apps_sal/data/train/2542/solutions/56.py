class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        if A[-1] - A[0] > 0:
            signal = 'incr'
        elif A[-1] - A[0] == 0:
            signal = 'same'
        elif A[-1] - A[0] < 0:
            signal = 'decr'

        if signal == 'same':
            if A == [A[0]] * len(A):
                return True
            else:
                return False

        elif signal == 'incr':
            for i in range(1, len(A)):
                if A[i] < A[i - 1]:
                    return False
            return True

        elif signal == 'decr':
            for i in range(1, len(A)):
                if A[i] > A[i - 1]:
                    return False
            return True
