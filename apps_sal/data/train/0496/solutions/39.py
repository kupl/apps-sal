class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        c = collections.Counter(A)
        mv = 0
        need = 0
        for i in sorted(c):
            mv += max(need - i, 0) * c[i] + c[i] * (c[i] - 1) // 2
            need = max(need, i) + c[i]
        return mv
