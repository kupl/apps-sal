class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        isIncreasing = True
        isDecreasing = True

        index = 1

        while index < len(A):

            previous = index - 1
            current = index

            if A[previous] < A[current]:
                isDecreasing = False

            if A[previous] > A[current]:
                isIncreasing = False
            index += 1

        return isIncreasing or isDecreasing
