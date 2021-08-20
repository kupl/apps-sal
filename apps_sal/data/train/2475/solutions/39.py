class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        if not A:
            return 0
        count = 0
        prev = ''
        for i in range(0, len(A[0])):
            for j in range(1, len(A)):
                if ord(A[j - 1][i]) > ord(A[j][i]):
                    count += 1
                    break
        return count
