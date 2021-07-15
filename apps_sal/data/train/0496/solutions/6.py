import collections
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        counter = collections.Counter(A)
        res = 0
        for i in range(80000):
            if counter[i] > 1:
                res += counter[i] - 1
                counter[i+1] += counter[i] - 1
        return res
