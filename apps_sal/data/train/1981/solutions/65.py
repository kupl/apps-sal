class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        a = [0] * (len(nums) + 1)
        for start, end in requests:
            a[start] += 1
            a[end + 1] -= 1
        for ind, val in enumerate(a[1:], 1):
            a[ind] += a[ind - 1]
        a.sort(reverse=True)
        total = 0
        for k, val in zip(a, nums):
            total += k * val
        return total % (10**9 + 7)
