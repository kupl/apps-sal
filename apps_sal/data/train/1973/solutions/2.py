class Solution:
    def isIdealPermutation(self, A):
        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True
