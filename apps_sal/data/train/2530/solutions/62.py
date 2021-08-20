class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        time = [x % 60 for x in time]
        dicts = {}
        for element in time:
            if element not in dicts:
                dicts[element] = 1
            else:
                dicts[element] += 1
        for i in range(len(time)):
            dicts[time[i]] -= 1
            target = 60 - time[i]
            if time[i] == 0:
                target = 0
            if target in dicts:
                res += dicts[target]
        return res
