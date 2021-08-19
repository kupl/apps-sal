class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        for c in range(len(A[0])):
            for i in range(len(A) - 1):
                if ord(A[i][c]) > ord(A[i + 1][c]):
                    count += 1
                    break
        return count
