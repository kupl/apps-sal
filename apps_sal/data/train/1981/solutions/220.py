class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        temp = [0] * (n + 1)

        for ind, i in enumerate(requests):
            s = i[0]
            e = i[1]
            temp[s] += 1
            temp[e + 1] -= 1

        for i in range(1, n + 1):
            temp[i] += temp[i - 1]

        temp = sorted(temp, reverse=1)
        nums = sorted(nums, reverse=1)

        ans = 0
        for i in range(n):
            ans += nums[i] * temp[i]

        return ans % ((10**9) + 7)
