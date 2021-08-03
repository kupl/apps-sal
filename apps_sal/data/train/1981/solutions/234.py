class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        calls = [0] * (len(nums) + 1)
        for start, end in requests:
            calls[start] += 1
            calls[end + 1] -= 1
        for i in range(1, len(calls)):
            calls[i] += calls[i - 1]
        calls.sort(reverse=True)
        nums.sort(reverse=True)
        return sum([i * j for i, j in zip(calls[:-1], nums)]) % (10**9 + 7)
