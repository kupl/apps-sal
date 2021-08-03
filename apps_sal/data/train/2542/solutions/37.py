class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 1:
            return True

        increasing = True
        decreasing = True

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                increasing = False

        if not increasing:
            for i in range(len(A) - 1):
                if A[i] < A[i + 1]:
                    decreasing = False

        return True if increasing or decreasing else False
