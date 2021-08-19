from collections import Counter


class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        c = Counter()
        for t in time:
            d = t % 60
            ans += c[(60 - t) % 60]
            c[d] += 1
        return ans
