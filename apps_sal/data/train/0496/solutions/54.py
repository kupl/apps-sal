class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = 0
        A = sorted(A)

        for i in range(len(A) - 1):
            increment = max(0, A[i] - A[i + 1] + 1)
            A[i + 1] += increment
            count += increment

        return count
