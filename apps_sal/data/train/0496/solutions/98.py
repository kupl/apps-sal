from collections import defaultdict


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:

        histogram = defaultdict(int)
        for num in A:
            histogram[num] += 1

        count = 0
        taken = []
        for num in range(0, 100000):
            if num in histogram and histogram[num] > 1:
                taken += [num] * (histogram[num] - 1)
            elif taken and num not in histogram:
                count += num - taken.pop()
        return count
