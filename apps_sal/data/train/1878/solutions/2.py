from itertools import accumulate


class Solution:

    def maxChunksToSorted(self, arr):
        right_min = list(accumulate(arr[::-1], lambda m, a: min(m, a)))[::-1]
        right_min = right_min[1:] + [float('inf')]
        left_max = list(accumulate(arr, lambda m, a: max(m, a)))
        return sum((1 for (x, y) in zip(left_max, right_min) if x <= y))
