class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = [0] * 60  # counter
        res = 0

        for t in time:
            theOther = -t % 60
            # 1. t%60 = 0
            # 2. t%60 != 0, 查找满足 t%60 + x%60=60的x的个数
            res += c[theOther]
            c[t % 60] += 1

        return res
