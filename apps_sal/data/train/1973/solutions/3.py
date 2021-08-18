class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        l = []
        [1, 0, 3, 2]
        if len(A) == 1:
            return True
        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True
