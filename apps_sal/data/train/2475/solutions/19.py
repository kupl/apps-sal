class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res = 0
        for i in range(len(A[0])):
            for j in range(1, len(A)):
                if A[j][i] < A[j - 1][i]:
                    res += 1
                    break

        return res
