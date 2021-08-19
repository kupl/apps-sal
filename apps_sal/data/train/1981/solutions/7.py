from heapq import *


class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        nums.sort(reverse=True)
        j = 0
        s = 0
        cnts = []
        n = len(nums)
        count = [0] * (n + 1)
        for (i, j) in requests:
            count[i] += 1
            count[j + 1] -= 1
        for i in range(1, n + 1):
            count[i] += count[i - 1]
        count.sort(reverse=True)
        s = 0
        for i in range(len(nums)):
            if count[i] > 0:
                s += count[i] * nums[i]
            else:
                break
        return s % MOD
