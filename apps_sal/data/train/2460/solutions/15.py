class Solution:

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def dac(X):
            if len(X) == 1:
                return X[0], X[0], X[0], X[0]

            n = len(X)
            nby2 = n // 2
            A = X[:nby2]
            B = X[nby2:]
            l1, r1, m1, s1 = dac(A)
            l2, r2, m2, s2 = dac(B)
            l = max(l1, s1 + l2)
            r = max(r2, s2 + r1)
            m = max(m1, m2, r1 + l2)
            s = s1 + s2
            return l, r, m, s

        return dac(nums)[2]
