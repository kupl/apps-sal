class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        isIncreasing, isDecreasing = True, True

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                isIncreasing = False
            elif A[i] < A[i + 1]:
                isDecreasing = False

        return isIncreasing or isDecreasing
