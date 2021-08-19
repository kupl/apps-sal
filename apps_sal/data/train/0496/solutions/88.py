class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        ret = 0
        for i in range(1, len(A)):
            p = A[i - 1]
            c = A[i]
            if p >= c:
                ret += p - c + 1
                A[i] = p + 1
        return ret
