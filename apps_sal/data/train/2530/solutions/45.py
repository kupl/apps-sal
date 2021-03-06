class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        import numpy as np
        (res, count) = (0, [0] * 60)
        for one in range(len(time)):
            index = time[one] % 60
            res += count[(60 - index) % 60]
            count[index] += 1
        return res
