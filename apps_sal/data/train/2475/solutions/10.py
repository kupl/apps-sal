class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        total_deletes = 0
        for j in range(len(A[0])):
            for i in range(1, len(A)):
                if A[i-1][j] > A[i][j]:
                    total_deletes += 1
                    break
        
        return total_deletes

