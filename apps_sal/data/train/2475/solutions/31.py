class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        m = len(A)
        n = len(A[0])
        res = 0
        for j in range(n):
            for i in range(m - 1):
                if A[i][j] > A[i + 1][j]:
                    res += 1
                    break
        return res
