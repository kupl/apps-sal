class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = [0] * 60
        res = 0
        for t in time:
            res += c[-t % 60]
            print(-t % 60, res, c[-t % 60])
            c[t % 60] += 1
        return res
