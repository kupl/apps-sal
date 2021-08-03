class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        result = 0
        count = [0] * 60
        for i in time:
            count[i % 60] += 1
        for n in range(1, 30):
            result += count[n] * count[60 - n]

        # 0, 30 independently
        result += count[0] * (count[0] - 1) // 2
        result += count[30] * (count[30] - 1) // 2

        return result
