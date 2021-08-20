class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        fre = [0] * 60
        for t in time:
            fre[t % 60] += 1
        for i in range(31):
            if i == 0 or i == 30:
                if fre[i] > 1:
                    count += fre[i] * (fre[i] - 1) // 2
            else:
                count += fre[i] * fre[60 - i]
        return count
