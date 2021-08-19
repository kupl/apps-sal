# brute force
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res = 0
        for j in range(len(A[0])):
            for i in range(len(A) - 1):
                if ord(A[i][j]) > ord(A[i + 1][j]):
                    res += 1
                    break
        return res
