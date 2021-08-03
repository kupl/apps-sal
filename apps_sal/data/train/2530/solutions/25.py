from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mem = defaultdict(int)
        res = 0

        for t in time:
            res += mem[(60 - t % 60) % 60]
            mem[t % 60] += 1

        return res
