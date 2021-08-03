from collections import defaultdict


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0] * len(nums)
        for i, j in requests:
            arr[i] += 1
            if j + 1 < len(arr):
                arr[j + 1] -= 1
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]

        arr.sort()
        nums.sort()
        res = 0

        for i, j in zip(arr, nums):
            res += (i * j)

        return res % (10**9 + 7)
