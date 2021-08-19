class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        return all([A[i] >= A[i - 1] for i in range(1, n)]) or all([A[i] <= A[i - 1] for i in range(1, n)])
