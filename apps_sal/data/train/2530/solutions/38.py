class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = {}
        res = 0
        for i in time:
            if (60 - (i%60) in dic) or (i%60 == 0 and 0 in dic):
                if i%60:
                    res += dic[60 - (i%60)]
                else:
                    res += dic[i%60]
            try:
                dic[i%60] += 1
            except KeyError:
                dic[i%60] = 1
        return res
