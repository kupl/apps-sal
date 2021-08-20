class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        A.sort()
        next_available = A[0]
        res = 0
        for a in A:
            if a >= next_available:
                next_available = a + 1
            else:
                res += next_available - a
                next_available += 1
        return res
