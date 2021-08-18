class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        max_value = A[0]
        for i in range(1, len(A) - 1):
            if A[i + 1] < max_value:
                return False
            if A[i] > max_value:
                max_value = A[i]
        else:
            return True
