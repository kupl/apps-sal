class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        nums.sort(reverse=True)
        N = len(nums)

        events = [0] * (N + 1)

        for start, end in requests:
            events[start] += 1
            events[end + 1] -= 1

        for i in range(1, len(events)):
            events[i] += events[i - 1]

        res = 0
        events.pop()

        events.sort()
        nums.sort()

        for num, size in zip(nums, events):
            res += num * size

        return res % MOD
