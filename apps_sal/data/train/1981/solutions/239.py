class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0] * (len(nums) + 1)
        for (s, e) in requests:
            arr[s] += 1
            arr[e + 1] -= 1
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        arr.pop()
        arr.sort()
        res = 0
        for (i, v) in enumerate(sorted(nums)):
            res += v * arr[i]
            res %= 10 ** 9 + 7
        return res
