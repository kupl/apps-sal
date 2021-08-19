class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # Need to have a count
        # Sort the array.
        result = 0
        A.sort()

        # Start from position 1 and traverse to end.
        for i in range(1, len(A)):
            # Check previous value >= current value
            # If so, increment A[i] by A[i-1] + 1
            if (A[i - 1] >= A[i]):
                result += A[i - 1] - A[i] + 1
                A[i] = A[i - 1] + 1

        # Return count
        return result
