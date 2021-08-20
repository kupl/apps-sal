class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = {}
        result = 0
        for tim in time:
            div_60 = tim % 60
            found = 0 if div_60 == 0 else 60 - div_60
            if found not in count:
                count[found] = 0
            result += count[found]
            if div_60 not in count:
                count[div_60] = 0
            count[div_60] += 1
        return result
