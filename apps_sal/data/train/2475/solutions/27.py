class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum([x[i] for x in A] != sorted([x[i] for x in A]) for i in range(len(A[0])))        
