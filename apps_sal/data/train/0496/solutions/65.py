class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        res = 0
        expect = 0
        for i in sorted(A):
            res += max(expect - i, 0)
            expect = max(i + 1, expect + 1)
        return res
