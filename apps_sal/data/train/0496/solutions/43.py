class Solution:

    def minIncrementForUnique(self, A):
        bar = -1
        res = 0
        for a in sorted(A):
            if a < bar:
                res += bar - a
            bar = max(bar + 1, a + 1)
        return res
