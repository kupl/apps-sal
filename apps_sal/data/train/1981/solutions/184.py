class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        A = nums
        count = [0 for _ in range(n + 1)]
        for r in requests:
            start = r[0]
            end = r[1]
            count[start] += 1
            count[end + 1] -= 1
        for i in range(1, n + 1):
            count[i] += count[i - 1]
        count = sorted(count, reverse=True)
        nums = sorted(nums, reverse=True)
        res = 0
        for i in range(len(count)):
            if count[i] == 0:
                break
            res += nums[i] * count[i]
        return res % (10 ** 9 + 7)
