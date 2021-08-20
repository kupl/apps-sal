class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr = [0] * 60
        for t in time:
            arr[t % 60] += 1
        res = 0
        for i in range(31):
            if i == 0 or i == 30:
                res += arr[i] * (arr[i] - 1) // 2
            else:
                res += arr[60 - i] * arr[i]
        return res
