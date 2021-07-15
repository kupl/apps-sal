class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(any(A[j][i] < A[j - 1][i] for j in range(1, len(A))) for i in range(len(A[0])))
