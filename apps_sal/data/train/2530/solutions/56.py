class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dct = {}
        count = 0
        for x in time:
            if x % 60 == 0 and 0 in dct:
                count += dct[x % 60]
            elif 60 - x % 60 in dct:
                count += dct[60 - x % 60]
            dct[x % 60] = dct.get(x % 60, 0) + 1
        return count
