class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        for i in range(len(time)):
            time[i] %= 60

        target = collections.defaultdict(int)
        count = 0
        for i in range(len(time)):
            if (60 - time[i]) % 60 in target:
                count += target[(60 - time[i]) % 60]
            target[time[i]] += 1

        return count
