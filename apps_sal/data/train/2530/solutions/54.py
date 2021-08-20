class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = [0] * 60
        res = 0
        for t in time:
            theOther = -t % 60
            res += c[theOther]
            c[t % 60] += 1
        return res
