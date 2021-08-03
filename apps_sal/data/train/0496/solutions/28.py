class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        counter = collections.Counter(A)
        taken = []
        result = 0

        for i in range(100000):
            if counter[i] > 1:
                taken.extend([i] * (counter[i] - 1))
            elif taken and counter[i] == 0:
                result += (i - taken.pop())
        return result
