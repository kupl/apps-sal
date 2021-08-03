class Solution:
    def isIdealPermutation(self, A):
        i = 0
        while i < len(A) - 1:
            if A[i] == i:
                i += 1
            elif A[i] == i + 1 and A[i + 1] == i:
                i += 2
            else:
                return False
        return True
