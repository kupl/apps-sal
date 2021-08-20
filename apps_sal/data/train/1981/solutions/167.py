class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count = [0] * len(nums)
        for request in requests:
            count[request[0]] += 1
            if request[1] < len(nums) - 1:
                count[request[1] + 1] -= 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        count.sort(reverse=True)
        nums.sort(reverse=True)
        res = 0
        for i in range(len(nums)):
            res += nums[i] * count[i]
        return res % (10 ** 9 + 7)
