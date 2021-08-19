class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        set_dim = 0
        for column in range(len(A[0])):
            for row in range(len(A) - 1):
                if A[row][column] > A[row + 1][column]:
                    set_dim += 1
                    break
        return set_dim
