from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        maxtime = max(time)
        timedict = defaultdict(int)
        for t in time:
            timedict[t] += 1

        pairs = 0
        for t in time:
            for matching_time in range(60 - t % 60, maxtime + 1, 60):
                if matching_time in timedict:
                    pairs += timedict[matching_time] - (t == matching_time)
        return pairs // 2
