class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        increasing = all((A[i] <= A[i + 1] for i in range(len(A) - 1)))
        decreasing = all((A[i] >= A[i + 1] for i in range(len(A) - 1)))
        return increasing or decreasing
