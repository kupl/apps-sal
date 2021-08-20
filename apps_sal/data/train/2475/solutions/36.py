class Solution:

    def minDeletionSize(self, A):
        word_len = len(A[0])
        count = 0
        for j in range(word_len):
            for i in range(1, len(A)):
                if A[i][j] < A[i - 1][j]:
                    count += 1
                    break
        return count
