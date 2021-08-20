class Solution:

    def numPairsDivisibleBy601(self, time: List[int]) -> int:
        res = 0
        total = {}
        for i in range(len(time)):
            temp = time[i] % 60
            try:
                total[temp].append(i)
            except KeyError:
                total[temp] = [i]
        for t in total.keys():
            if t == 0:
                res = res + len(total[0]) * (len(total[0]) - 1) // 2
            if t == 30:
                res = res + len(total[30]) * (len(total[30]) - 1) // 2
            if 0 < t < 30 and 60 - t in total.keys():
                res = res + len(total[t]) * len(total[60 - t])
        return res

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        total = collections.defaultdict(list)
        res = 0
        for i in range(len(time)):
            total[time[i] % 60].append(i)
        for t in total:
            if t == 0 or t == 30:
                res += len(total[t]) * (len(total[t]) - 1) // 2
            elif 0 < t < 30 and 60 - t in total:
                res += len(total[t]) * len(total[60 - t])
        return res
