class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n = len(A[0])
        res = 0
        for i in range(n):
            col = [a[i] for a in A]
            if col != sorted(col):
                res += 1
        return res
