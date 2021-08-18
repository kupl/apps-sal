from collections import Counter


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        c = 0

        sn = list(sorted(nums))
        starts, ends = Counter(), Counter()

        for s, e in requests:
            starts[s] += 1
            ends[e + 1] += 1

        repeats = []
        ranges = 0
        for i, _ in enumerate(nums):
            ranges += starts[i] - ends[i]
            repeats.append(ranges)

        sr = list(sorted(repeats))
        for i, r in enumerate(repeats):
            c += sn[i] * sr[i]

        return c % MOD
