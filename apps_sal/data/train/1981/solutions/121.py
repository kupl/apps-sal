from itertools import permutations


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        count = [0 for i in range(len(nums) + 1)]
        for start, end in requests:
            count[start] += 1
            count[end + 1] -= 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        count.sort(reverse=True)
        maxSum = 0
        for i in range(len(count) - 1):
            maxSum += count[i] * nums[i]
        return maxSum % (10 ** 9 + 7)
