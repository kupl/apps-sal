class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = collections.Counter(A)

        taken = []

        mv = 0

        for i in range(80000):
            if count[i] > 1:
                taken.extend([i] * (count[i] - 1))
            elif taken and count[i] == 0:
                mv += (i - taken.pop())
        return mv
