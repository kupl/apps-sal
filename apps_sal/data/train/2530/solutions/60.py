from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        store = defaultdict(int)
        pair = 0

        for t in time:
            if (60 - t) % 60 in store:
                pair += store[(60 - t) % 60]

            store[t % 60] += 1

        return pair
