class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        from collections import defaultdict
        hashmap = defaultdict(int)
        res = 0
        for t in time:
            if t % 60 in hashmap:
                res += hashmap[t % 60]
            if t % 60 == 0:
                hashmap[0] += 1
                continue
            hashmap[60 - t % 60] += 1
        return res
