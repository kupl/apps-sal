class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        # Valid monotic number of the following characteristic
        # Increasing
        # Decreasing
        # None increasing or decreasing

        # Linear time complexity is the best thing to do.

        isIncreasing = True
        isDecreasing = True

        # check if the number is Monotonic
        index = 1

        while index < len(A):

            previous = index - 1
            current = index

            # In any given if the current number is bigger then number is increasing
            # So assign isIncreasing to false
            if A[previous] < A[current]:
                isDecreasing = False

            # if the current is smaller the number is decreasing
            # so assign isIncreasing to false
            if A[previous] > A[current]:
                isIncreasing = False
            index += 1

        return isIncreasing or isDecreasing
