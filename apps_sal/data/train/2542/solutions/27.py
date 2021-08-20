class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        is_increasing = is_decreasing = True
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                is_decreasing = False
            if A[i] > A[i - 1]:
                is_increasing = False
        return is_decreasing or is_increasing
