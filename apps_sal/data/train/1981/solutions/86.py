class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ok = [0] * (len(nums) + 1)
        for i in requests:
            ok[i[0]] += 1
            ok[i[1] + 1] -= 1
        ok = [0] + ok
        for i in range(1, len(ok)):
            ok[i] += ok[i - 1]
        ok = ok[1:-1]
        ok.sort(reverse=True)
        ans = 0
        nums.sort(reverse=True)
        for i in range(len(nums)):
            ans += nums[i] * ok[i]
        return ans % 1000000007
