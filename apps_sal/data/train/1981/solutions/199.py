class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        len_nums = len(nums)
        frequencies = [0] * (len_nums + 1)
        for start, end in requests:
            frequencies[start] += 1
            frequencies[end + 1] -= 1
        for k in range(1, len_nums):
            frequencies[k] += frequencies[k - 1]
        frequencies.sort(reverse=True)
        nums.sort(reverse=True)
        max_sum = 0
        for k in range(len_nums):
            max_sum += nums[k] * frequencies[k]
        return max_sum % (10**9 + 7)
