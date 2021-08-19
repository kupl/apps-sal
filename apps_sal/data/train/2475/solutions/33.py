class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        t = 0
        i = 0
        while i < len(A[0]):
            j = 0
            last = chr(0)
            while j < len(A):
                if A[j][i] >= last:
                    last = A[j][i]
                else:
                    t += 1
                    break
                j += 1
            i += 1
        return t
