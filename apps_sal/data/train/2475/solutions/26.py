class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        indiciesToRemove = []
        columns = len(A[0])
        rows = len(A)
        for col in range(0, columns):
            previous = chr(0)
            for row in range(0, rows):
                if A[row][col] < previous:
                    indiciesToRemove.append(col)
                    break
                previous = A[row][col]
        return len(indiciesToRemove)
