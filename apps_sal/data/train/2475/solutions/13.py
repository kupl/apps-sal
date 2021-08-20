class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        rows = len(A)
        cols = len(A[0])
        for c in range(cols):
            for r in range(rows - 1):
                if A[r][c] > A[r + 1][c]:
                    count += 1
                    break
        return count
