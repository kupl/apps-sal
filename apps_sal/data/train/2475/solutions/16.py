class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n = len(A[0])
        del_indices = []
        for j in range(n):
            for i in range(len(A) - 1):
                if A[i][j] > A[i + 1][j]:
                    del_indices.append(j)
                    break
            continue
        return len(del_indices)
