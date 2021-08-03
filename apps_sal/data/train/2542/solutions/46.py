class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        is_decreasing = is_increasing = True
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                is_increasing = False
            if A[i] > A[i + 1]:
                is_decreasing = False
        return is_decreasing or is_increasing
