class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        times = [0] * (len(nums) + 1)
        for a, b in requests:
            times[a] += 1
            times[b + 1] -= 1
        for i in range(1, len(times)):
            times[i] += times[i - 1]
        times.pop()
        times.sort()
        return sum(a * b for a, b in zip(times, nums)) % (10**9 + 7)
