from collections import Counter


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = Counter(time)
        pair = 0
        for p in count:
            tp = count[p]
            t = 60 - p % 60
            while t <= 500:
                if t != p:
                    pair += tp * count[t]
                else:
                    pair += tp * (tp - 1)
                t += 60

        return pair // 2
