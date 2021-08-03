class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if not time:
            return 0
        arr = [0] * 60

        for x in time:
            arr[x % 60] += 1

        res = arr[0] * (arr[0] - 1)
        res += arr[30] * (arr[30] - 1)
        for i in range(1, 30):
            if arr[i]:
                res += arr[i] * arr[60 - i]
        for i in range(31, 60):
            if arr[i]:
                res += arr[i] * arr[60 - i]
        return res // 2
