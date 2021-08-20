class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        result = 0
        for i in range(len(A[0])):
            last = A[0][i]
            for j in range(1, len(A)):
                if ord(last) > ord(A[j][i]):
                    result += 1
                    break
                last = A[j][i]
        return result
