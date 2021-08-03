class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        if not set(B).issubset(set(A)):
            return -1

        max_rep = len(B) // len(A) + 3
        A_new = A

        for i in range(1, max_rep):
            if B in A_new:
                return i
            A_new += A
        return -1
