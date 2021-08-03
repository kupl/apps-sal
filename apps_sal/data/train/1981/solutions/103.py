from typing import List
import collections


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        sweeplines = []
        for i, j in requests:
            sweeplines.append((i, 1))
            sweeplines.append((j + 1, -1))
        sweeplines.sort()
        sweeplines = collections.deque(sweeplines)
        freq = 0
        freqs = []
        for i in range(len(nums)):
            while sweeplines and sweeplines[0][0] == i:
                freq += sweeplines[0][1]
                sweeplines.popleft()
            freqs.append(freq)
        freqs.sort(reverse=True)
        nums.sort(reverse=True)
        ans = sum([freq * num for freq, num in zip(freqs, nums)])
        return ans % (10**9 + 7)
