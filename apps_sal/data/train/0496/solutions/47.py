class Solution:
    def minIncrementForUnique(self, A):
        res = need = 0
        for i in sorted(A):
            res += max(need - i, 0)
            need = max(need + 1, i + 1)

        return res
