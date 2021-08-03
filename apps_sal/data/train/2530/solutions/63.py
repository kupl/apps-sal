class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        lookup = collections.defaultdict(int)
        count = 0
        for time in time:
            key = -time % 60
            if key in lookup:
                count += lookup[key]
            lookup[time % 60] += 1
        return count
