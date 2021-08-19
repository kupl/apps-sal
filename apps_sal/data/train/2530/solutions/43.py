class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        map = [0] * 60
        for t in time:
            rem = t % 60
            comp = 60 - rem
            if map[comp % 60] > 0:
                count += map[comp % 60]
            map[t % 60] += 1
        return count
